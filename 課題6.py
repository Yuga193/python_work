#問題１
buy_list=["りんご", "イチゴ", "パイナップル"]
fruits={"りんご": 100, "バナナ": 80, "イチゴ": 200, "キウイ": 150, "メロン": 500, "パイナップル": 400}
A=0
for B in buy_list:
    A+=fruits[B]
print(f"合計{A}円のお買い物になりました") 

#問題２
order_list=["マルゲリータ", "マリナーラ", "クワトロフォルマッジ"]
pizza={"マルゲリータ": 1000, "マリナーラ": 1200, "カプリチョーザ": 1400, "クワトロフォルマッジ": 1600}
C=0
for D in order_list:
    C+=pizza[D]
print(f"お会計は{C}円となります") 

#問題３
shopping_list=["りんご", "バナナ", "チーズ", "ヨーグルト"]
quantity={"りんご": 5, "バナナ": 3, "チーズ": 2, "ヨーグルト": 1}
E=0
for F in shopping_list:
    E+=quantity[F]
print(f"合計で{E}個書いました") 

#問題４
grades = [
{"name": "Alice", "math": 80, "english": 75, "science": 90},
{"name": "Bob", "math": 90, "english": 85, "science": 95},
{"name": "Charlie", "math": 70, "english": 65, "science": 80},
{"name": "David", "math": 60, "english": 55, "science": 70}
]

MATH=[student["math"] for student in grades]
MATH_TOTAL=sum(MATH)
MATH_frequency=len(MATH) 
print(f"数学の平均点は{MATH_TOTAL/MATH_frequency}点です")

ENGLISH=[student["english"] for student in grades]
ENGLISH_TOTAL=sum(ENGLISH)
ENGLISH_frequency=len(ENGLISH) 
print(f"英語の平均点は{ENGLISH_TOTAL/ENGLISH_frequency}点です")

SCIENCE=[student["science"] for student in grades]
SCIENCE_TOTAL=sum(SCIENCE)
SCIENCE_frequency=len(SCIENCE) 
print(f"理科の平均点は{SCIENCE_TOTAL/SCIENCE_frequency}点です")

for student in grades:
    if student["name"]=="Alice":
        ALICE=[student.get("math"), student.get("english"), student.get("science")]
ALICE_TOTAL=sum(ALICE)
ALICE_frequency=len(ALICE) 
print(f"アリスさんの平均点は{ALICE_TOTAL/ALICE_frequency}点です")

for student in grades:
    if student["name"]=="Bob":
        BOB=[student.get("math"), student.get("english"), student.get("science")]
BOB_TOTAL=sum(BOB)
BOB_frequency=len(BOB) 
print(f"ボブさんの平均点は{BOB_TOTAL/BOB_frequency}点です")

for student in grades:
    if student["name"]=="Charlie":
        CHARLIE=[student.get("math"), student.get("english"), student.get("science")]
CHARLIE_TOTAL=sum(CHARLIE)
CHARLIE_frequency=len(CHARLIE) 
print(f"チャーリーさんの平均点は{CHARLIE_TOTAL/CHARLIE_frequency}点です")

for student in grades:
    if student["name"]=="David":
        DAVID=[student.get("math"), student.get("english"), student.get("science")]
DAVID_TOTAL=sum(DAVID)
DAVID_frequency=len(DAVID) 
print(f"デイビッドさんの平均点は{DAVID_TOTAL/DAVID_frequency}点です")

SUBJECTS=len(grades[0].keys())-1
TOTAL_SUBJECTS=len(grades)*SUBJECTS
TOTAL_SCORE=MATH_TOTAL+ENGLISH_TOTAL+SCIENCE_TOTAL
print(f"全科目の平均点は{TOTAL_SCORE/TOTAL_SUBJECTS}点です")

#問題５
members = [   
{"name": "アリス", "age": 20, "gender": "女性", "sports": ["バスケットボール", "テニス"]},
{"name": "ボブ", "age": 25, "gender": "男性", "sports": ["野球", "サッカー", "バレーボール"]},
{"name": "チャーリー", "age": 30, "gender": "男性", "sports": ["テニス", "ゴルフ"]},
{"name": "デイビッド", "age": 35, "gender": "男性", "sports": ["スイミング"]}
]

basketball_players=[member for member in members if "バスケットボール" in member["sports"]]
print("バスケットボールをする人のリスト")
print(basketball_players)

males=[member for member in members if member["gender"]=="男性"]
print("男性のリスト")
print(males)

over_30age=[member for member in members if member["age"]>=30]
print("年齢が30以上の人のリスト")
print(over_30age)

golf_female = any(member["gender"] == "女性" and "ゴルフ" in member["sports"] for member in members)
Golf_female = "はい" if golf_female else "いいえ"
print("ゴルフをする女性はいるかどうか")
print(Golf_female)