"""
=============================
ᕕ(◠ڼ◠)ᕗ
@time:2024/4/22 12:07
@IDE:PyCharm
=============================
"""
import os

# from PIL import Image
# import os
# import tkinter as tk
# from tkinter import filedialog
#
# def reduce_image_size(im, target_size_kb):
#     output_dir = 'picture'
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)
#     name = input('文件名为：')
#     file_name = os.path.join(output_dir, name+'.jpg')
#
#     # 转换图片为RGB模式，去除透明通道
#     if im.mode != 'RGB':
#         im = im.convert('RGB')
#
#     for quality in range(100, 0, -1):  # 从高质量向低质量调整
#         im.save(file_name, 'JPEG', quality=quality, optimize=True)
#         # 检查文件大小是否接近目标大小
#         if os.path.getsize(file_name) / 1024 <= target_size_kb:
#             break  # 如果达到或低于目标大小，则停止调整
#
#     print(f"最终压缩质量: {quality}, 文件大小: {os.path.getsize(file_name) / 1024:.2f} KB")
#
# def sol():
#     root = tk.Tk()
#     root.withdraw()
#     file_path = filedialog.askopenfilename(
#         title='请选择文件',
#         filetypes=[('Image Files', '*.png;*.jpg;*.jpeg')]
#     )
#
#     if file_path:
#         im = Image.open(file_path)
#         try:
#             target_size_kb = int(input('请输入你想要的图片大小（例如：300KB）：\n'))
#             reduce_image_size(im, target_size_kb)
#             print('图片已修改并保存。')
#         except ValueError:
#             print("请输入有效的整数值。")
#         except Exception as e:
#             print(f"发生错误：{e}")
#     else:
#         print("没有选择任何文件。")
#
#     root.destroy()
#
# if __name__ == '__main__':
#     sol()

from PIL import Image
import tkinter as tk
from tkinter import filedialog
import os

def reduce_size(img, target_size):
    file_pith = 'picture'
    if not os.path.exists(file_pith):
        os.mkdir(file_pith)
    name_pictrue = input('请输入保存后的文件名:')

    output_pictrue = os.path.join(file_pith, name_pictrue+'.jpg')

    if img.mode !='RGB':
        img = img.convert('RGB')

    for quality in range(100, 0, -1):
        img.save(output_pictrue, 'JPEG', quality=quality, optimize=True)
        if os.path.getsize(output_pictrue)/1024 <= target_size:
            break

    print('最终降低画质为：{}'.format(os.path.getsize(output_pictrue)/1024))
    print('图片修改完成，已保存在{}'.format(output_pictrue))

def sol():
    root = tk.Tk()
    root.withdraw()
    img_filepath = filedialog.askopenfilename()
    if img_filepath:
        img = Image.open(img_filepath)
        try:
            target_size = int(input('请输入目标画质大小：（eg: 300kb）\n'))
            reduce_size(img, target_size)
        except ValueError:
            print('请输入正确的画质大小格式（int)')
        except Exception as e:
            print(f'print(f"发生错误：{e}")')
    else:
        print('没有选择文件')

    root.mainloop()

if __name__ == '__main__':
    sol()