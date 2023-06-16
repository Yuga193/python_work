
import random

class Janken:
    HANDS=["グー", "チョキ", "パー"]

    @staticmethod
    def A():
        return random.choice(Janken.HANDS)


class JankenGame:
    def __init__(self):
        self.win = 0
        self.lose = 0
        self.draw = 0

    def B(self,player_hand,computer_hand):
        if player_hand==computer_hand:
            self.draw+=1
            return "あいこです。"
        elif (player_hand=="グー"and computer_hand=="チョキ") or (player_hand=="チョキ" and computer_hand=="パー") or (player_hand=="パー" and computer_hand=="グー"):
            self.win+=1
            return "あなたの勝ちです！"
        else:
            self.lose+=1
            return "あなたの負けです…"

    def C(self):
        print("勝ち: "+str(self.win)+", 負け: "+str(self.lose)+", 引き分け: "+str(self.draw))

    def play(self):
        while True:
            print("じゃんけんを始めます")
            player_hand=input("グー、チョキ、パーのどれかを入力してください: ")

            if player_hand not in Janken.HANDS:
                print("もう一度入力をお願いします")
                continue

            computer_hand=Janken.A()
            print("コンピュータの出した手: "+computer_hand)
            result=self.B(player_hand,computer_hand)
            print(result)
            self.C()

            if self.win==3:
                print("あなたが3勝しました。ゲーム終了！")
                break

game=JankenGame()
game.play()
