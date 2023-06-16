def A(n):
    if n <= 1:  
        print(f"{n}は素数ではありません")
        return
    elif n == 2:
        print(f"{n}は素数です")
        return
    for i in range(2, n):  
        if n % i == 0: 
            print(f"{n}は素数ではありません")
            return 
    print(f"{n}は素数です")  

while True:
    try:
        B = int(input("数値を入力してください:"))
        A(B)
        break  
    except ValueError:  
        print("正の整数を入力してください。")



#sympyモジュールを使用してやる方法(こっちの方が短く実践向けだが、pipでのインストールが必要なため環境によっては動作しない)

#from sympy import isprime
#while True:
#    try:
#        C=int(input("数値を入力してください: "))
#        break
#    except ValueError:
#        pass
#if isprime(C):
#    print("素数です")
#else:
#    print("素数ではありません")