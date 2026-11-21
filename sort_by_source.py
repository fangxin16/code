import os
import shutil

# 待整理的文件夹：从手机/相机导出来的东西全堆在这里
base = r"C:\Users\芳忻\Desktop\code\测试素材"

# 后缀清单：用来判断它是视频还是图片
视频后缀 = ['.mp4', '.mov', '.avi', '.mkv']
图片后缀 = ['.jpg', '.jpeg', '.png', '.webp', '.gif']

# 来源只能靠文件名里的关键词认：电脑看不到"谁发给你的"
微信线索 = ['mmexport', 'wechat', '微信']
截图线索 = ['screenshot', 'screen_shot', '截图']

for 文件名 in sorted(os.listdir(base)):
    路径 = os.path.join(base, 文件名)

    # 目录跳过，只处理文件
    if not os.path.isfile(路径):
        continue

    小写名 = 文件名.lower()
    后缀 = os.path.splitext(文件名)[1].lower()

    # 不是图片也不是视频的，一律不动
    if 后缀 not in 视频后缀 and 后缀 not in 图片后缀:
        continue

    是不是视频 = 后缀 in 视频后缀

    # 先认来源，来源优先：微信的东西哪怕里面是视频，也进微信
    if any(线索 in 小写名 for 线索 in 微信线索):
        大类 = "微信\\" + ("视频" if 是不是视频 else "照片")
    elif any(线索 in 小写名 for 线索 in 截图线索):
        大类 = "截图"
    elif 是不是视频:
        大类 = "视频"
    else:
        大类 = "照片"

    目标目录 = os.path.join(base, "整理后", 大类)
    os.makedirs(目标目录, exist_ok=True)

    shutil.move(路径, os.path.join(目标目录, 文件名))
    print(文件名, "->", 大类)
