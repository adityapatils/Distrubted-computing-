#Load balancer
#load_balancer.py
import random

class LoadBalancer:
    def __init__(self, servers):
        # Initialize the list of servers
        self.servers = servers

    def random_selection(self):
        # Randomly select a server from the list
        return random.choice(self.servers)

def simulate_client_requests(load_balancer, num_requests):
    # Simulate client requests
    for i in range(num_requests):
        print(f"Request {i+1}: ", end="")
        
        # Using Random algorithm for load balancing
        server_random = load_balancer.random_selection()
        
        # Print the selected server for the request
        print(f"Random - Server {server_random}")

# List of available servers
servers = ["Server A", "Server B", "Server C"]

# Create a LoadBalancer instance
load_balancer = LoadBalancer(servers)

# Simulate 10 client requests
simulate_client_requests(load_balancer, 10)
