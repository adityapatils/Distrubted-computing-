#RMI PC
import Pyro4

@Pyro4.expose
class PalindromeChecker(object):
    
    def is_palindrome(self, text):
        # Remove spaces and convert to lowercase
        text = text.lower().replace(" ", "")
        
        # Check if the text is equal to its reverse
        return text == text[::-1]

# Create a Pyro daemon
daemon = Pyro4.Daemon()

# Register the PalindromeChecker object with the daemon
uri = daemon.register(PalindromeChecker)

print("URI:", uri)

# Start the Pyro daemon
daemon.requestLoop()
