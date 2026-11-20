import os

# 要整理的大文件夹：里面装着一堆以数字命名的子文件夹
base = r"C:\Users\芳忻\Desktop\code\测试图片"

# 只把这些后缀当成图片处理，别的文件不动
图片后缀 = ['.jpg', '.jpeg', '.png', '.webp', '.gif']

# 一层一层看 base 里的东西
for folder in os.listdir(base):
    文件夹路径 = os.path.join(base, folder)

    # 不是文件夹的跳过
    if not os.path.isdir(文件夹路径):
        continue

    # 拿到这个文件夹里的所有文件，按名字排好队
    文件列表 = sorted(os.listdir(文件夹路径))
    编号 = 1

    for 文件名 in 文件列表:
        后缀 = os.path.splitext(文件名)[1].lower()

        # 不是图片的跳过
        if 后缀 not in 图片后缀:
            continue

        旧路径 = os.path.join(文件夹路径, 文件名)
        新文件名 = folder + "-" + str(编号) + 后缀
        新路径 = os.path.join(文件夹路径, 新文件名)

        os.rename(旧路径, 新路径)
        print(旧路径, "->", 新文件名)
        编号 = 编号 + 1
