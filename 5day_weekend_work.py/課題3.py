while True:
    try:
        A=int(input("最初の整数を入力してください: "))
        break
    except ValueError:
        print("整数を入力してください")

while True:
    try:
        B=int(input("2番目の整数を入力してください: "))
        break
    except ValueError:
        print("整数を入力してください")

print(f"入力した２つの和は{A+B}です")
