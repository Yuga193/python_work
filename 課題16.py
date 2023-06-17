#問題１
import random

player_number=int(input("あなたが選ぶ数字（1〜6）: "))
numbers=list(range(1, 7)) 
numbers.remove(player_number) 
friend_number=random.choice(numbers) 

print(f"友人が選んだ数字は {friend_number} です。")

winner=None

for i in range(10):
    roll=random.randint(1, 6) 
    print(f"出目は{roll}です。")
    if roll==player_number:
        winner="あなた"
        break
    if roll==friend_number:
        winner="友人"
        break
if winner:
    print(f"{winner}の勝ちです！")
else:
    print("残念でした、両者引き分けです")


#問題２
import random

def B(start,end):
    n=random.randint(2,10)#ここでリスト内の要素数のランダム生成
    return [random.randint(start, end) for i2 in range(n)]

numbers=B(0,50)

print(f"作成されたリストは{numbers}")
total=sum(numbers)

if total>=100:
    print(f"合計は{total}ですので目標達成です！")
else:
    print(f"合計は{total}ですので目標未達成です…")


#問題３
def temperature():
    temp_input=input("変換前の温度とその単位を入力してください (例:20C,68F): ")
    temp=float(temp_input[:-1])
    temp_unit=temp_input[-1]

    if temp_unit.upper()=="C":
        FC=(temp*9/5)+32
        print(f"変換後の温度:{FC:.2f}F")#.2fで少数第２位まで表示
    elif temp_unit.upper()=="F":
        FC=(temp-32)*5/9
        print(f"変換後の温度:{FC:.2f}C")#.2fで少数第２位まで表示
    else:
        print("未知の単位が入力されました")

temperature()

#問題４
def calculation():
    try:
        number1=float(input("1つ目の値を入力してください:"))
    except ValueError:
        print("数値ではないので入力し直してください")
        return
    operator=input("演算子(+,-.*,/)を入力してください:")
    try:
        number2=float(input("2つ目の値を入力してください:"))
    except ValueError:
        print("数値ではないので入力し直してください")
        return

    if operator=="+":
        answer=number1+number2
    elif operator=="-":
        answer=number1+number2
    elif operator=="*":
        answer=number1*number2
    elif operator=="/":
        if number2!=0:  #除算で割る数が0だとエラー吐くので０以外の数値だけを計算するようにする
            answer=number1/number2
        else:
            print("すみません。０では割れません")
            return
    else:
        print("演算子の入力が間違えています")
    print(f"{answer:.2f}")

calculation()