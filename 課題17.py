import time

max_bath=float(input("お風呂の最大容量を入力してください(単位はL): "))
water=float(input("毎分の水の量をLで入力してください(単位はL): "))
now_bath=0.0

while True:
    now_bath+=water
    print(f"現在の水量: {now_bath}L")

    if now_bath>=max_bath:
        print("お風呂が満水になりました")
        break
    time.sleep(60)#ここでリアルタイムで60秒(1分)待機させます！便利なタイマー機能！



#一応１４行目で待機させたけど、実際に沸かすわけじゃないから省略でも良い気はしてます。ただ課題は便利なタイマー作ろうなので・・・
#実際に試すときは１４行目は絶対にコメントアウトする。もしくは値を１にすること勧めます。値によってはめっちゃ待機時間長いです！


