#RMI PC
#server.py
#client.py
#naman
import Pyro4

def main():
    # Input the URI of the server
    uri = input("Enter server URI: ")
    
    # Create a proxy object to connect to the server
    checker = Pyro4.Proxy(uri)
    
    # Input a string to check for palindrome
    text = input("Enter a string to check if it's a palindrome: ")
    
    # Check if the text is a palindrome using the remote method
    is_palindrome = checker.is_palindrome(text)
    
    if is_palindrome:
        print(f"'{text}' is a palindrome.")
    else:
        print(f"'{text}' is not a palindrome.")

if __name__ == "__main__":
    main()
