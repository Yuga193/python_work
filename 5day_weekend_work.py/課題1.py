print("自分の名前")#(1)

print("自分の名前\nカタカナ\n年齢")#(2)

A="自分の名前"#(3)
B=50
C=1.6
print(A+"さん")
print(str(B)+"kg")
print(str(C)+"m")
print("BMIは"+str(B/(C**2))+"です")

D=12#(4)
E=15
print(f"""{D}+{E}
{D+E}""")

F=float(input("体重を入力してください:"))#(5)
print(f"入力された体重は{F}kgです")
