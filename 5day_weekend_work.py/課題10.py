A=int(input("好きな値を与えてください:"))
for B in range(1, A+1):
    if B%3==0:
        if B%5==0:
            print("Fizz Buzz")
        else:
            print("Fizz")
    elif B%5==0:
        print("Buzz")
    else:
        print(B)