# Distributed Data Processing with Apache Spark  

This project explores the implementation of **Apache Spark** for distributed computing by developing and analyzing three fundamental algorithms: **Word Count**, **Dijkstra’s Shortest Path**, and **Page Rank**. Through this work, I gained hands-on experience in processing large-scale datasets efficiently, applying graph-based algorithms, and understanding Spark’s execution framework.

### Key Components:
- **Word Count Algorithm**: A text-processing application where Spark reads large text files, normalizes the data by handling case sensitivity and punctuation, removes stop words, and computes word frequencies. The results are sorted by frequency.
- **Dijkstra’s Shortest Path Algorithm**: Designed to compute the shortest path between nodes in a graph. The graph structure, stored as text files, was processed using Spark to determine the shortest distances from a given source node to all other nodes.
- **Page Rank Algorithm**: Simulated a network of interconnected web pages and applied the Page Rank algorithm to determine the importance of each page based on link structures.

## Environment Setup  
The project was developed using **PySpark** within the **Apache Spark** framework. To set up and execute the project, follow these steps:

1. **Install Apache Spark** by referring to the [official PySpark documentation](https://spark.apache.org/docs/latest/api/python/getting_started/install.html).
2. **Obtain Text Data**: The Word Count and Page Rank algorithms require text input. Datasets from **Project Gutenberg** or any other publicly available sources can be used.
3. **Execute the Scripts**: The provided Python scripts load and process the data, compute algorithm outputs, and generate result files. Additionally, Spark’s WebUI was utilized to analyze job execution and monitor computational stages.

# Spark Streaming K-mer Counting Project  
 
This project demonstrates the use of **Apache Spark Streaming** to process real-time data streams and count the occurrences of k-mers (subsequences of length `k`) in text data. The project implements a **k-mer counting program** using PySpark and Spark Streaming to process continuous input data streamed from a TCP socket. Specifically, the program processes a generated text file (`sentences.txt`) and streams data through the TCP port `9999` to count 3-mers (k-mers of length 3).
