fibonacci = [0,1]

print("Enter the Nth Fibonacci number you wish to")
print("calculate (such as 5, 50, 1000 ,9999), or QUIT to quit")
n = int(input("> "))


count = 0

for i in range(n-2):
    next_number = fibonacci[0 + count] + fibonacci[1 + count]
    fibonacci.append(next_number)
    count += 1

print(*fibonacci, sep=", ")



# fix nth number of 0 and 1 printing 0,1
# make QUIT actually work
# Display a warming if the nth value is above 10000
# try to do the finboonaci sequence with a while loop