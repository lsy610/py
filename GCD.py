a = int(input("請輸入第一個數："))
b = int(input("請輸入第二個數："))

while b != 0:
    r = a % b
    a = b
    b = r

print("最大公约数是:", a)