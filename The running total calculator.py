print("The running total calculator")
total = 0
while True:
    number_or_done=input("Enter a number or 'done': ")
    if number_or_done=="done":
        break
    else:
        total+= int(number_or_done)

print("--- Final Calculation ---")
print(f"The final sum of all numbers is: {total}")
