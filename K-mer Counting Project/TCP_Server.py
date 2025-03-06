import socket
import time

HOST = "localhost"
PORT = 9999
FILE_PATH = "sentences.txt"
SLEEP_INTERVAL = 10  # Seconds to wait between sending lines

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1) # maximum number of queued connections 

print(f"Server is running and waiting for a connection on {HOST}:{PORT}...")

# Accept a connection from a client (your Spark Streaming program)
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}.")

try:
    with open(FILE_PATH, "r") as file:
        for line in file:
            client_socket.sendall(line.encode("utf-8"))  # Send each line to the client
            print(f"Sent: {line.strip()}")
            time.sleep(SLEEP_INTERVAL)  # Simulate streaming delay
except FileNotFoundError:  # if file not found
    print(f"Error: File '{FILE_PATH}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    client_socket.close()
    server_socket.close()
    print("Server closed.")