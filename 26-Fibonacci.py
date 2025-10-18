import sys

print("Enter the Nth Fibonacci number you wish to")
print("calculate (such as 5, 50, 1000 ,9999), or QUIT to quit")

def get_response():
    response = input("> ").upper()
    return response

response = get_response()
if response == "QUIT":
    print("Thanks for playing!!")
    sys.exit()
elif response.isdecimal() and int(response) != 0:
    nth = int(response)
else:
    print()
    print("Please enter a number greater than 0, or QUIT")
    get_response()

def fibonacci():
    count = 0
    fibonacci_list = [0,1]
    for i in range(nth - 2):
        next_number = fibonacci_list[0 + count] + fibonacci_list[1 + count]
        fibonacci_list.append(next_number)
        count += 1

    print(*fibonacci_list, sep=", ")

match nth:
    case 0:
        print("The #1 numbers in a fibonacci sequence is 0")
    case 1:
        print("The #2 numbers in a fibonacci sequence is 1")
    case x if x > 10000:
        print("WARNING: This wil take a while to display on the")
        print("screen. If you want to quit this program before it is")
        print("done, press Ctrl-C")
        input("Press Enter to begin...")
        fibonacci()
    case _:
        fibonacci()
        


# a, b = 0, 1

# count = 0

# nth_terms = int(input("Enter the nth value: "))

# print("Fibonacci")
# while (count <= nth_terms ):
#     print(a, sep=", ")
#     nth = a + b
#     a = b
#     b = nth
#     count += 1


# fix nth number of 0 and 1 printing 0,1 ✅
# make QUIT actually work ✅
# Display a warming if the nth value is above 10000 ✅
# try to do the fibonacci sequence with a while loop ✅