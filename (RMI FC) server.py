#RPC FC 
from xmlrpc.server import SimpleXMLRPCServer

# Define the factorial function to calculate factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Create an XML-RPC server instance listening on localhost and port 8000
server = SimpleXMLRPCServer(('localhost', 8000))

# Register the factorial function with the server, giving it a name 'calculate_factorial'
server.register_function(factorial, 'calculate_factorial')

# Print a message to indicate the server is listening
print("Server listening on port 8000...")

# Start the server and keep it running
server.serve_forever()
