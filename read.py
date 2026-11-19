def fail_count(scores):
    fail = 0
    for s in scores:
        if s < 60:
            fail = fail + 1
    return fail
f = open("scores.txt", "r", encoding="utf-8")
text = f.read()
f.close()
lines = text.split()      # 按空白切开，变成几段
scores = []               # 空篮子
for x in lines:
    scores.append(int(x)) # 一个个人进去，顺手转成整数

print(scores)
print(fail_count(scores))