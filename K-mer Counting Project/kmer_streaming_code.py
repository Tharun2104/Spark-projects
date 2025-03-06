from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext

conf = SparkConf().setAppName("KMerCount").setMaster("local[2]")
sc = SparkContext(conf=conf)
ssc = StreamingContext(sc, 10)  # Batch interval of 10 seconds

checkpointDir = "/Users/tharun/checkpoint"
ssc.checkpoint(checkpointDir)

# Define the input stream from TCP socket
lines = ssc.socketTextStream("localhost", 9999)

# Function to extract k-mers of length 3 from each line  
def extract_kmers(line, k=3):
    if not line: # Ensure the line is not empty
        return []
    words = line.split()  # Split the line into words(if the input has some spaces)
    kmers = []
    for word in words:
        if len(word) >= k:  # Only process words that are long enough for k-mers
            kmers.extend([word[i:i + k] for i in range(len(word) - k + 1)])
    return kmers

# Applying k-mers for each line
kmers = lines.flatMap(lambda line: extract_kmers(line))

# Map k-mers to (kmer, 1) pairs
kmer_pairs = kmers.map(lambda kmer: (kmer, 1))

# Define the function to update the state with new k-mer counts
def update_kmer_count(new_values, running_count):
    if running_count is None:
        running_count = 0
    # Update the running count by adding the new values
    return sum(new_values) + running_count

# Updating the k-mer counts across batches using updateStateByKey
kmer_counts = kmer_pairs.updateStateByKey(update_kmer_count)

# Sort the k-mer counts
top_kmers = kmer_counts.transform(lambda rdd: rdd.sortBy(lambda x: x[1], ascending=False))
top_kmers.pprint()

# Start the streaming context
ssc.start()
ssc.awaitTermination()