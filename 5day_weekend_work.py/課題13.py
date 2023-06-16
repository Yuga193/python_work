A=float(input("身長を入力してください(単位cm)："))
B=float(input("体重を入力してください(単位kg)："))
C=A/100
D=B/(C**2)
print("BMIは"+str(D)+"です")