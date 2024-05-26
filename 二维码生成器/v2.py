"""
=============================
ᕕ(◠ڼ◠)ᕗ
@time:2024/5/26 18:00
@IDE:PyCharm
=============================
"""
from MyQR import myqr
import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os


def web():
    print("请输入你想让二维码包含的文字讯息或者要跳转的网站：")
    s = input()
    return s


def get_counter(output_dir):
    # 读取或初始化图片计数器
    counter_path = os.path.join(output_dir, 'counter.txt')
    if os.path.exists(counter_path):
        with open(counter_path, 'r') as file:
            counter = int(file.read().strip())
    else:
        counter = 0
    return counter


def update_counter(output_dir, counter):
    # 更新图片计数器
    counter_path = os.path.join(output_dir, 'counter.txt')
    with open(counter_path, 'w') as file:
        file.write(str(counter))


def sol(s, output_dir, img_counter):
    root = tk.Tk()
    root.withdraw()

    def on_closing():
        root.quit()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    img_filepath = filedialog.askopenfilename(title=f"请选择图片作为第{img_counter + 1}张二维码的封面")

    if img_filepath:
        img = Image.open(img_filepath)
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        output_filename = f'img{img_counter + 1}.png'
        output_path = os.path.join(output_dir, output_filename)
        try:
            myqr.run(
                words=s,
                version=20,
                picture=img_filepath,
                colorized=True,
                save_name=output_path
            )
            print(f'第{img_counter + 1}张二维码生成完毕！')
        except Exception as e:
            print(f'发生错误: {e}')
    else:
        print(f'第{img_counter + 1}张二维码未选择图片，生成取消。')

    root.destroy()


if __name__ == '__main__':
    output_dir = 'output_img'
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    print('请输入你想要生成的二维码数量：')
    n = int(input())
    img_counter = get_counter(output_dir)
    for i in range(n):
        s = web()
        print(f"正在为第{i + 1}张二维码选择图片...")
        sol(s, output_dir, img_counter + i)
    update_counter(output_dir, img_counter + n)
