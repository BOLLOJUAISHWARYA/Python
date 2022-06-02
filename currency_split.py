#currency splitting

number= int(input("Enter number : "))

def num_split(number):
    number = "{:,}".format(number)
    return number
    
after_split=num_split(number)
print(after_split)
