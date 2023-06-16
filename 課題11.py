import random

win=0
lose=0
draw=0

A=["グー", "チョキ", "パー"]

while True:
    print("じゃんけんを始めます")
    B=input("グー、チョキ、パーのどれかを入力してください: ")

    if B not in A:
        print("もう一度入力をお願いします")
        continue

    C=random.choice(A)
    print("コンピュータの出した手: "+C)

    if B==C:
        print("あいこです。")
        draw+=1
    elif (B=="グー"and C=="チョキ") or (B=="チョキ" and C=="パー") or (B=="パー" and C=="グー"):
        print("あなたの勝ちです！")
        win+=1
    else:
        print("あなたの負けです…")
        lose+=1
    print("勝ち: "+str(win)+", 負け: "+str(lose)+", 引き分け: "+str(draw))
    
    D=input("もう一度遊びますか？ (y/n): ")
    if D!="y":
        break
