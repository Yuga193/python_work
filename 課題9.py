#問題１
A=input("文字列をひらがなで入力してください: ")
B=A[::-1]
if A==B:
    print("入力された文字列は回文です")
else:
    print("入力された文字列は回文ではありません")

#問題２
import random
C=random.randint(1, 100)
if C>79:
        print("優")
elif C>59:
        print("良")
else:
    print("可")