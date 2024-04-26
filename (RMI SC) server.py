#RMI SC
import Pyro4

@Pyro4.expose
class StringConcatenator:
    
    def concatenate(self, str1, str2):
        # Concatenate the two input strings
        return str1 + str2

# Create a Pyro daemon
daemon = Pyro4.Daemon()

# Create a URI for the server object
uri = daemon.register(StringConcatenator)

print("URI:", uri)

# Start the Pyro daemon
daemon.requestLoop()
