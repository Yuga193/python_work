#問題１
import random

def A(n, start, end):#nでリストの個数、startで数値の最小値、ednで数値の最大値の設定
    return[random.randint(start, end) for _ in range(n)]

def B(numbers):
    even=[]
    odd=[]
    for num in numbers:
        if num%2==0:
            even.append(num)
        else:
            odd.append(num)
    return sorted(even), sorted(odd, reverse=True)

numbers=A(20, 1, 100)#ここでリストの数値は２０個、最小値は１、最大値は１００と指定。
even,odd=B(numbers)

print(f"数字リスト: {numbers}")
print(f"偶数: {even}")
print(f"奇数: {odd}")



#問題２
def C(n2, start2, end2):
    return[random.randint(start2, end2) for _ in range(n2)]

def E(D):
    no_duplicates=list(set(D)) 
    sorted_list=sorted(no_duplicates) 
    return sorted_list[:3] 

D=C(20,1,13)#ここは関数Aでも作用します
print(f"今回作成されたリストは{D}")
F=E(D)

print(f"最初の値３つは{F}")


#問題３
def G(H):
    words=list(H) 
    I=[word[::-1] for word in words]  
    J=I[::-1]  
    return ' '.join(J) 

WORD=input("好きな言葉を入力してください: ")
print(G(WORD))


#問題４
def randomlist(n3, start3, end3):
    return[random.randint(start3, end3) for _ in range(n3)]

def match(Cace1,Cace2):
    set1=set(Cace1)
    set2=set(Cace2)
    return list(set1&set2)

list1=randomlist(5,1,10)#ここは関数Aでも作用します
print(f"今回作成された1つ目のリストは{list1}")
list2=randomlist(5,1,10)#ここは関数Aでも作用します
print(f"今回作成された2つ目のリストは{list2}")

D=match(list1,list2)
print(f"重複する要素は{D}")


#問題5
def number():
    value=input("辞書に値を与えてください: ")
    original={"key":value}
    if value.isdigit():
        value=int(value)*2 
        new_dict={"key": value} 
    return original, new_dict

original,new_dict=number()
print(f"作成された辞書: {original}")
print(f"値が二倍にされた辞書: {new_dict}")