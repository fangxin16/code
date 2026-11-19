target = 7

while guess != target:
    guess = int(input("猜一个数字："))
    if guess < target:
        print("小了")
    elif guess > target:
        print("大了")
print("猜对了")