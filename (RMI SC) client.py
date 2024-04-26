#RMI SC
#server.py
#client.py
#adit
#ya
import Pyro4

def main():
    # Input the URI of the server
    uri = input("Enter URI of the server: ")
    
    # Create a proxy object to connect to the server
    concatenator = Pyro4.Proxy(uri)
    
    # Input the first string
    str1 = input("Enter string 1: ")
    
    # Input the second string
    str2 = input("Enter string 2: ")
    
    # Call the remote 'concatenate' method on the server with the input strings
    result = concatenator.concatenate(str1, str2)
    
    # Print the concatenated result returned by the server
    print("Concatenated String:", result)

if __name__ == "__main__":
    main()
