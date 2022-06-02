
#Taking input from user to count/print prime numbers

number=int(input("Enter a Number :"))

def prime_numbers(number):
    count = 0
    for num in range(2, number+1):
        for i in range(2, num):
               if (num % i) == 0:
                   break
        else:
            count += 1
            #print(num)

    return count 
 
a=prime_numbers(number)
print(a)
