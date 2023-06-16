import random
A=[random.randint(1, 100) for _ in range(10)]
print("・作成されたリスト")
print(A)

def find_max(lst):
    if not lst:  
        return None
    sorted_lst = sorted(lst,reverse=True)  
    return sorted_lst[0]

B=find_max(A)#完全にランダムな値のリストから最大値を引けるならどんなリストでも正常に動作する関数だと証明できます
print(f"このリストの中の最大値は{B}である")

C=[]#空のリストできちんとNoneと表示されるかどうかの確認
D=find_max(C)
print(D)

