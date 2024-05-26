"""
=============================
ᕕ(◠ڼ◠)ᕗ
@time:2024/5/25 21:52
@IDE:PyCharm
=============================
"""
from MyQR import myqr
import tkinter as tk
from tkinter import filedialog,simpledialog
from PIL import Image
import os

def web():
    # print("请输入你想让二维码包含的文字讯息或者要跳转的网站：")
    # s = input()
    # return s
    # 使用 tkinter 的 simpledialog 代替 input() 获取文本信息
    root = tk.Tk()
    root.withdraw()
    s = simpledialog.askstring("输入", "请输入你想让二维码包含的文字讯息或者要跳转的网站：")
    root.destroy()
    return s

def sol(s,output_dir, img_counter):

    root = tk.Tk()
    root.withdraw()
    # tk.Tk() 是 tkinter 模块中创建新窗口的标准方式。这个调用返回一个窗口对象，通常称为 root 或 main window，是所有其他GUI元素（如按钮、标签、文本框等）的容器。
    # 在这个例子中，变量 picture_root 被赋值为这个主窗口对象。虽然在这个脚本中我们不直接使用这个窗口来显示任何内容，但它是必需的，因为 tkinter 需要一个根窗口来管理其它GUI操作，如文件对话框。

    # withdraw() 方法用于隐藏主窗口。在此场景中，主窗口没有其他用途，我们不希望它出现在屏幕上，因为用户只需要进行文件选择。
    # 使用 withdraw() 可以使根窗口在屏幕上变为不可见，避免给用户带来不必要的界面干扰。这个窗口仍然存在于内存中，只是不显示出来。

    def on_closing():
        root.quit()

    root.protocol("WM_DELETE_WINDOW", on_closing)  # 在尝试关闭窗口时调用on_closing函数
    img_filepath = filedialog.askopenfilename()
    # filedialog.askopenfilename() 函数是 tkinter 的 filedialog 模块中的一个方法，用于弹出一个对话框，允许用户选择一个文件。这个方法会打开一个标准的操作系统文件选择窗口，用户可以浏览文件系统选择文件。
    # 当用户选择一个文件并点击“打开”按钮后，这个方法返回文件的完整路径。如果用户取消选择，通常返回一个空字符串。
    # 在这里，返回的文件路径被存储在变量 img_filepath 中，后续的代码可以使用这个路径来加载和处理用户选择的图片。

    # 这三行代码实际上是在设置一个后台运行的 tkinter 应用，用于获取用户想要处理的图片文件路径，但不显示任何多余的GUI元素。这是一种常见的方法，用于在需要文件输入但不需要完整GUI界面的脚本中集成 tkinter 的文件对话框功能。
    if img_filepath:
        img = Image.open(img_filepath)
        # 检查图片模式，转换为RGB如果是RGBA
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        # 修改扩展名为.png确保兼容性
        tail = '.png'
        output_filename = f'img{img_counter}' + tail
        output_path = os.path.join(output_dir, output_filename)
        try:
            myqr.run(
                words=s,  # 包含的信息，例如一个网站链接
                version=20,  # 提高版本号以增加二维码的初始大小
                picture=img_filepath,  # 背景图片路径
                colorized=True,  # 是否彩色
                save_name=output_path
            )
        except Exception as e:
            print(f'发生{e}错误')

    # 添加mainloop(): mainloop()是tkinter的核心，负责处理所有的GUI事件和更新。它通常放置在脚本的底部。
    # 使用quit()方法: 在文件选择后调用quit()可以结束mainloop()，这样可以关闭整个tkinter应用，避免程序挂起。
    # 使用protocol处理关闭事件: 这可以处理用户点击关闭按钮的事件，确保即使用户关闭了窗口，tkinter应用也能正确退出。
    else:
        print('没有选择文件')
    root.destroy()

if __name__ == '__main__':
    output_dir = 'output_img'
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    # print('请问你想要生成多少张？')
    # n = int(input())
        # 使用 tkinter 的 simpledialog 代替 input() 来获取二维码的数量
    root = tk.Tk()
    root.withdraw()
    n = simpledialog.askinteger("数量", "请问你想要生成多少张？")
    root.destroy()

    for i in range(n):
        s = web()
        print("请选择图片作为二维码的封面")
        sol(s, output_dir, i)
        print('生成完毕！')

