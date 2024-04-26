#RPC AO
#server.py
#client.py
#12
#3
#3
import xmlrpc.client

# Main function to interact with the XML-RPC server
def main():
    # Create a proxy object to connect to the server running on localhost and port 8000
    server = xmlrpc.client.ServerProxy('http://localhost:8000')

    while True:
        # Input the first number
        n1 = int(input("Enter the first number (or 0 to exit): "))
        
        # Check if the user wants to exit
        if n1 == 0:
            print("Exiting the program.")
            break
        
        # Input the second number
        n2 = int(input("Enter the second number: "))
        
        # Input the operation choice
        opp = int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, or 0 to exit: "))
        
        # Check if the user wants to exit
        if opp == 0:
            print("Exiting the program.")
            break
        
        # Call the remote 'calculate' function on the server with the inputs
        result = server.calculate(n1, n2, opp)
        
        # Print the result returned by the server
        print("Result:", result)

# Check if the script is being run as the main program
if __name__ == "__main__":
    main()
