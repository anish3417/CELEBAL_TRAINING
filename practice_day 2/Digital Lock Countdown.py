number = input("Enter a number: ")

while len(number) > 1:
    digit_sum= sum(int(a)for a in number)

    new_number =  int(number)-digit_sum


    number= str(new_number)



print(number)