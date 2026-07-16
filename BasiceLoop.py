shop = int(input("บอสสั่งให้ไปเก็บส่วยกี่ร้าน: "))
result = 0
for i in range(1,shop+1):
    money = float(input(f"เก็บเงินจากร้าน{i}: "))
    result+=money

print(f"เก็บครบ: {shop} ร้าน ได้เงินมาทั้งหมดจำนวน: {result} บาท")
