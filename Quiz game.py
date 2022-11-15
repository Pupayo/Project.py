print("ยินดีต้อนรับสู่เกมตอบคำถามนะ!!!")
print("เรื่อง เมืองหลวงของแต่ละประเทศ")
play = input("อยากจะเล่นรึเปล่าล่ะ??(อยากเล่นตอบว่า อยาก): ")

if play !=  "อยาก":
    quit()

print("งั้นก็ไปกันเลย!!!")
name = input("แต่ๆๆๆ ก่อนจะเล่นขอรู้จักชื่อนายหน่อยสิ: ")
score = 0

answer1 = input("เมืองหลวงของสเปนคือ??: ")
if answer1 == "มาดริด":
    print('ถูกต้อง!')
    score += 1
else:
    print("ผิด!")

answer2 = input("เมืองหลวงของลาวคือ??: ")
if answer2 == "เวียงจันทน์":
    print('ถูกต้อง!')
    score += 1
else:
    print("ผิด!")

answer3 = input("เมืองหลวงของอังกฤษคือ??: ")
if answer3 == "ลอนดอน":
    print('ถูกต้อง!')
    score += 1
else:
    print("ผิด!")

answer4 = input("เมืองหลวงของอิตาลีคือ??: ")
if answer4 == "โรม":
    print('ถูกต้อง!')
    score += 1
else:
    print("ผิด!")

answer5 = input("เมืองหลวงของบราซิลคือ??: ")
if answer5 == "บราซิเลีย":
    print('ถูกต้อง!')
    score += 1
else:
    print("ผิด!")

print("คะแนนของ"+name+"คือ",score,"ขอบคุณที่มาเล่นนะ!!")
    