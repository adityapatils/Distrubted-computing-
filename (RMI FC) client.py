#RPC FC
#server.py
#client.py
#10
import xmlrpc.client

# Main function to interact with the XML-RPC server
def main():
    # Create a proxy object to connect to the server running on localhost and port 8000
    server = xmlrpc.client.ServerProxy('http://localhost:8000')
    
    # Ask user to input a number
    n = int(input("Enter the number: "))
    
    # Call the remote 'calculate_factorial' function on the server with the input number
    result = server.calculate_factorial(n)
    
    # Print the result returned by the server
    print("Factorial of", n, "is:", result)

# Check if the script is being run as the main program
if __name__ == "__main__":
    main()
