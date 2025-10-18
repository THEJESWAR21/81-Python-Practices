a, b = 0, 1

count = 0

nth_terms = int(input("Enter the nth value: "))

print("Fibonacci")
while (count <= nth_terms ):
    print(a, sep=", ")
    nth = a + b
    a = b
    b = nth
    count += 1

