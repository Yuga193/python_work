print("自分の名前")#(1)

A=input("名前を入力してください:")#(2)
print("こんにちは。"+A+"さん")

import random#(3)
B=[random.randint(1, 100) for _ in range(10)]
print(B)
C=random.choice(B)
D=random.choice(B)
print(f"1つ目の数値は{C}です")
print(f"2つ目の数値は{D}です")
print(f"2つの数値の乗は{C*D}となります")

#(4)
while True:
    try:
        E=float(input("お好きな値を入力してください:"))
        break
    except ValueError:
        print("入力されたものは数値ではありませんので再入力お願いします")

while True:
    try:
        F=float(input("お好きな値をもう一つ入力してください:"))
        break
    except ValueError:
        print("入力されたものは数値ではありませんので再入力お願いします")

print(f"その合計は{E+F}となります")
