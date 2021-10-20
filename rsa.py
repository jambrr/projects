import string

def encryption():
    print("Encryption")
    print(
    '''Required parameters
        - n
        - e
        - msg''')
    n = int(input("n = "))
    e = int(input("e = "))
    msg = input("msg = ")

    msg = int(string.ascii_lowercase.index(msg))

    cipherText = pow(msg, e, n)

    print(cipherText)


def decryption(d, n):
    print("Decryption")
    print(
    '''Required parameters
        - n
        - d''')

    n = int(input("n = "))
    e = int(input("d = "))
    msg = input("cipher msg = ")



if __name__ == "__main__":
    print("Welcome to the rsa application")
    print("Options")
    print("1 - encryption")
    print("2 - decryption")
    option = input("Enter options here: ")

    if(option == "1"):
        encryption()
    elif(option == "2"):
        decryption(1,2)
    else:
        print("Invalid input")


