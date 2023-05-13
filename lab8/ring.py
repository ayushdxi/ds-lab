import socket

# Configuration
NUM_NODES = 5  # Number of participating nodes
COORDINATOR_PORT = 5000  # Port number for the initial coordinator node

# Create sockets for each node
sockets = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for _ in range(NUM_NODES)]

# Bind sockets to ports and listen for incoming connections
for i, sock in enumerate(sockets):
    port = COORDINATOR_PORT + i
    sock.bind(('localhost', port))
    sock.listen(1)

# Function to send a message to the next node in the ring
def send_message(node_id, message):
    next_node_id = (node_id + 1) % NUM_NODES
    next_node_port = COORDINATOR_PORT + next_node_id
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sender_sock:
        sender_sock.connect(('localhost', next_node_port))
        sender_sock.sendall(message.encode())

# Function to receive a message from the previous node in the ring
def receive_message(node_id):
    current_node_port = COORDINATOR_PORT + node_id
    conn, addr = sockets[node_id].accept()
    with conn:
        data = conn.recv(1024)
        return data.decode()

# Start the ring algorithm
def run_ring_algorithm(node_id):
    print(f"Node {node_id} joining the ring...")

    # Wait for the previous node to initiate the algorithm
    receive_message(node_id)

    # Send the message to the next node to initiate the election
    send_message(node_id, f"ELECTION {node_id}")

    # Wait for the response from the next node
    response = receive_message(node_id)
    sender_id = int(response.split()[1])

    # Compare IDs to determine the new coordinator
    if sender_id > node_id:
        new_coordinator_id = sender_id
    else:
        new_coordinator_id = node_id

    # Inform the next node about the new coordinator
    send_message(node_id, f"COORDINATOR {new_coordinator_id}")

    print(f"Node {node_id} has completed the algorithm.")

# Main execution
if __name__ == "__main__":
    # Start the coordinator node (Node 0)
    print("Starting the coordinator node...")
    run_ring_algorithm(0)

    # Start the remaining nodes
    for i in range(1, NUM_NODES):
        run_ring_algorithm(i)
