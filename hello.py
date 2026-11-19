scores = [80, 90, 70, 58, 45]
fail = 0
for s in scores:
    if s < 60:
        fail = 1
print("不及格人数：", fail)
