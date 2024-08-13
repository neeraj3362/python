Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = int(input("Enter a number: "))
... 
... if num == 1:
...     print(num, "is not a prime number")
... elif num > 1:
...    for i in range(2,num):
...        if (num % i) == 0:
...            print(num,"is not a prime number")
...            print(i,"times",num//i,"is",num)
...            break
...    else:
...        print(num,"is a prime number")
... else:
...    print(num,"is not a prime number")
