print( "-----Movie Ticket Pricer-----")

children_age=int(input("Please,enter your age:  "))
if children_age<=12:
    print("You fall into the Children category")
    print("Your ticket price is $8")
elif children_age>12:
    print("Your age is too high for the children's ticket")

    adult_age=int(input("What's your age? "))
    if 13<adult_age<65: 
      print("You fall into the Adult category")
      print("Your ticket price is $15")

      senior_age=int(input("What's your age ,dear sir/madam? "))
if 64<senior_age:
   print("You fall into the Senior Category")
   print("Your ticket price is $10")
else:
   print("Error")
   
   