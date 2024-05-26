"""
=============================
ᕕ(◠ڼ◠)ᕗ
@time:2024/5/25 21:36
@IDE:PyCharm
=============================
"""
import os


def check_file(filename):
    # 检查文件是否存在
    if not os.path.exists(filename):
        return "文件不存在，请检查路径和文件名。"

    # 检查文件扩展名
    if not filename.lower().endswith(('.jpg', '.png', '.bmp', '.gif')):
        return "文件格式不正确。请使用 jpg, png, bmp, 或 gif 格式的文件。"

    return "文件检查通过，可以使用。"


# 替换以下文件名为你的文件名和路径
filename = 'D:\project_bymyself\project\画质降低\pictrue\picture\涩图.jpg'
print(check_file(filename))
