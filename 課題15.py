#問題１
import random 

def A(n,start,end):
    return[random.randint(start, end) for _ in range(n)]
numbers=A(3,0,5)#ここの３のところを０にしていただければ空のリストに変わります

def sum1(numbers):
    goukei=sum(numbers)
    return goukei

print(numbers)
total=sum1(numbers)
print(total)


#問題２
def counter(string,substring):
    string=string.lower()
    substring=substring.lower()
    return string.count(substring)

ALICE="""Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, 'and what is the use of a book,' thought Alice 'without pictures or conversations?"""
Sister="sister"
print("原文")
print(ALICE)
print(f"原文の中から探したい単語は{Sister}")
print(f"原文の中にその単語は{counter(ALICE,Sister)}回使われています")

#ユーザー入力に変更したい場合は２３行目〜２８行目をコメントアウトして、下記の３１行目〜３３行目を有効にしてください
#ALICE=input("適当な英文を入力してください:")
#Sister=input("数えたい英単語を入力してください:")
#print(counter(ALICE,Sister))




#問題３
def switch_kv():
    Key=input("辞書にキーを与えてください: ")
    value=input("辞書に値を与えてください: ")
    original={Key:value}
    new_dict={value:Key}
    return original, new_dict

original,new_dict=switch_kv()
print(f"作成された辞書: {original}")
print(f"入れ替わった辞書: {new_dict}")


#問題４
def create_list():
    listA=input("カンマで区切られた文字や数値を入力してください: ")
    listB=listA.split(",")
    return listB

def merge_list(list1, list2):
    merged=[]
    for a, b in zip(list1, list2):
        merged.append(a)
        merged.append(b)
    return merged

list1=create_list()
list2=create_list()

merged_list=merge_list(list1, list2)
print("マージしたリスト: ", merged_list)