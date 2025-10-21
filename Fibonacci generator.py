print("--- Fibonacci Sequence Generator ---")
numbers=int(input("How many Fibonacci numbers would you like to generate?  "))
a,b=0,1
for i in range(numbers):
    print("a,end=")
    a, b = b, a + b
    print()

