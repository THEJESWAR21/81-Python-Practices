# A, 2 ---> C

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt():
    # TODO: Add a Try Catch block here for Error handling

    print("Please enter the key (number) to use.")
    key = int(input("> "))

    print("is it (L)eft Swtich or (R)ight Switch")
    switch = input("> ").upper()

    print("Enter the message to encrypt?")
    message = str(input("> ")).upper()

    for i in message:
        encrypted_message = ""
        char_index = alphabet.find(i)

        while key <= 25:
            if i.isalpha() and i != " ":
                if switch == "R":
                    encrypted_char = alphabet[char_index] + key
                elif switch == "L":
                    encrypted_char = alphabet[char_index] - key





def decrypt():
    print("Please enter the key (number) to use.")
    key = int(input("> "))

    print("Enter the message to decrypt?")
    message = str(input("> ")).upper()


def main():
    print("Do you want to (e)ncrypt or (d)ecrypt?")
    option = input(">").upper()

    if option == "E":
        encrypt()
    elif option == "D":
        decrypt()
        
main()
