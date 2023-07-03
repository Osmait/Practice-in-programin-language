number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

for num in number:
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} fizz buzz")
    elif num % 3 == 0:
        print(f"{num} fizz")
    elif num % 5 == 0:
        print(f"{num} buzz")
    else:
        print(num)
        

    