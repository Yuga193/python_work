#問題１
A={"フランスパン":10, "ロールパン":10, "クロワッサン":10, "パン・オ・ショコラ":10}
for B, C in A.items():
    print(f"{B}の在庫数: {C}")

#問題２
number_list=[1, 3, 5, 7, 9]
sum=0
for i in number_list:
    sum+=i
    print(sum)

#問題３
D= ["コーヒー", "紅茶", "ハンバーガー", "スープ", "サンドイッチ"]
print("カフェのメニュー")
for E in D:
    print("・"+E)
    
#問題４
from tabulate import tabulate
F=list(range(1, 10))
G=[" "]+F
table=[[H]+[H*I for I in F] for H in F]
print(tabulate(table, headers=G, tablefmt="pipe"))