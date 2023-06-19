import random
money=10000
deck=[2,3,4,5,6,7,8,9,10,"J","Q","K","A"]*4
playerWIN=0#この二つは５勝するか５敗した場合に終了の処理をする時に使います
playerLOSE=0

#deckリスト内の文字を数値に変換を関数
def card_value(hand):
    result=0
    for card in hand:
        if card in ["K","Q","J"]:
            result+=10
        elif card=="A":
            continue
        else:
            result+=card
    return result

#Aを引いた際に１か１１か選択する処理を行う関数
def ace_value():
    while True:
        value=input("エースを引きました。エースを1としますか、それとも11としますか？(1 または 11): ")
        if value in ["1","11"]:
            return int(value)
        else:
            print("無効な入力です。もう一度お試しください。")

#ゲームの開始処理
def game():
    global money #global変数にして値が変動するようにしてます
    global playerWIN
    global playerLOSE

    print(f"現在の所持金は{money}円です")
    while True:
        try:
            play_money=int(input("いくら賭けますか？:"))
            if play_money<=money:
                break
            else:
                print("所持金を超えています")
        except ValueError:
            print("無効な入力です。数値を入力してください。")#tryとValueErrorといういつものやつで数値以外の入力を全て弾いています
    money-=play_money
    print(f"現在の所持金は{money}円となりました")
    player_hand=[random.choice(deck)]
    dealer_hand=[random.choice(deck)]
    if player_hand[0]=="A":#ここの一連の処理がないとAを引いた時に挙動がおかしくなります
        player_hand[0]=ace_value()
    if dealer_hand[0]=="A":
        dealer_hand[0]=ace_value()
    print("プレイヤーのカード:", player_hand)
    print("ディーラーの1枚目のカード",dealer_hand)
    next_card=random.choice(deck)
    if next_card=="A":
        next_card=ace_value()
    player_hand.append(next_card)
    print("プレイヤーのカード:",player_hand," 現在の値:",card_value(player_hand))


    #NPCの手札処理
    while card_value(dealer_hand)<17: #１７以下なら引くよって処理。種明かしをすると実はここで初めてディーラーは2枚目のカードを引いてますし、18以上になるまで無限に引きます
        dealer_hand.append(random.choice(deck))

    #長いループ
    while True:
        hand_value=card_value(player_hand)#ここでJ,Q,Kを関数使用して１０に変換
        if "A" in player_hand:#Aがあったときの処理です
            num_aces=player_hand.count("A")#ここでAの枚数を把握し、複数枚引いていたとしても対応できるようにしている
            for _ in range(num_aces):
                if "A" in player_hand:
                    ace=ace_value()
                    hand_value+=ace
                    player_hand.remove("A")
        if hand_value>21:#21超えたら負けだよっていうだけの話
            playerLOSE+=1
            return"プレイヤーの負け（バスト）"
        if hand_value==21:
            if card_value(dealer_hand)==21:
                money+=play_money
                return"ブラックジャック！ 引き分け！"
            else:
                print(f"ディーラーのカード:{dealer_hand}")
                money+=(play_money*2.5)
                playerWIN+=1
                return"ブラックジャック！プレイヤーの勝ち！"

        #プレイヤー側が勝負か引くかの選択。ｙでカード追加処理
        player_choice=input("追加で引くか (引く = y, 勝負 = n): ").lower()
        if player_choice=='y':
            next_card=random.choice(deck)
            if next_card=="A":
                next_card=ace_value()
            player_hand.append(next_card)
            print("プレイヤーのカード:",player_hand," 現在の値:",card_value(player_hand))
        elif player_choice=='n':
            break #breakしなければ６６行面に戻るループ処理です

    print("ディーラーのカード:",dealer_hand," 現在の値:",card_value(dealer_hand))
    
    #勝敗判定。ここで初めてプレイヤーとディーラーの手札を比較しています
    if card_value(dealer_hand)>21:
        money+=(play_money*2)
        playerWIN+=1
        return"ディーラーの負け（バスト）"
    elif card_value(dealer_hand)==21:
        playerLOSE+=1
        return"ブラックジャック！ ディーラーの勝ち！"
    elif card_value(dealer_hand)>hand_value:
        playerLOSE+=1
        return"ディーラーの勝ち！"
    elif card_value(dealer_hand)<hand_value:
        playerWIN+=1
        money+=(play_money*2)
        return"プレイヤーの勝ち！"
    else:
        money+=play_money
        return"引き分け！"

while True: #再戦処理
    print(game())
    print(f"現在の戦歴は{playerWIN}勝{playerLOSE}敗")
    if playerWIN>=5:
        print("5勝したのでゲーム終了です")
        print(f"最終的な所持金は{money}円でした")
        play_again = input("再度プレイしますか？(y/n): ").lower()
        money=10000
        if play_again !='y':
            break
    if playerLOSE>=5:
        print("5敗したのでゲーム終了です")
        print(f"最終的な所持金は{money}円でした")
        play_again = input("再び最初からプレイしますか？(y/n): ").lower()
        money=10000
        if play_again !='y':
            break
    if money<=0:
        print("所持金が０になったのでゲーム終了です")
        break

#要点のまとめ
#まず前提として29行目から118行目までgameという大きな関数で構成されています
#returnとbreakでループから抜けます(これはこのプログラムに限った話ではない)
#game関数は所持金の表示、賭け金の設定、カードの配布、数値の比較を行っています
#A,J,Q,Kの処理は全て関数であり、game関数に組み込んで使用しています
#主な流れとしてはgame関数使用、戦歴の表示、５勝もしくは５敗の条件を満たしておらず所持金がある場合は再びgame関数使用に戻るという感じです




#エンドレスモード。こちらで遊ぶ時は下記のコメントアウトを解除した後に１１９行目~１３８行目をコメントアウト
#while True: #再戦処理
#    print(game())
#    print(f"現在の所持金は{money}円です")
#    if money<=0:
#        print("残念ですがお金が足りないようです")
#        break
#    play_again=input("再度プレイしますか？(y/n): ").lower()
#    if play_again !='y':
#        break