print("--- Triangle Pattern Printer ---")
height=int(input("Please, enter the height of a triangle: "))


for i in range(1,height+1): 
    for j in range(i):
        print("*", end=" ")
      
    print()