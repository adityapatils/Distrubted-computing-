#RPC AO
from xmlrpc.server import SimpleXMLRPCServer

# Define the arithmetic function to perform arithmetic operations
def arithmetic(n1, n2, opp):
    if opp == 1:
        return n1 + n2
    elif opp == 2:
        return n1 - n2
    elif opp == 3:
        return n1 * n2
    elif opp == 4:
        # Check for division by zero
        if n2 != 0:
            return n1 / n2
        else:
            return "Division by zero not allowed"
    else:
        return "Not an operator"

# Create an XML-RPC server instance listening on localhost and port 8000
server = SimpleXMLRPCServer(('localhost', 8000))

# Register the arithmetic function with the server, giving it a name 'calculate'
server.register_function(arithmetic, 'calculate')

# Inform that the server is listening
print("Server listening on port 8000...")

# Start the server and keep it running
server.serve_forever()
