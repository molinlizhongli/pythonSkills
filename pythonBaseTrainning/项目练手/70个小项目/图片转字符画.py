# _*_ coding = utf-8 _*_
# @Date : 2021/11/8
# @Time : 17:43
# @NAME ：molin

from PIL import Image
import argparse

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 命令行输入参数处理
parser = argparse.ArgumentParser()
parser.add_argument('file') # 输入文件
parser.add_argument('-o', '--output') # 输出文件
parser.add_argument('--width', type = int, default = 80) #输出字符画宽
parser.add_argument('--height', type = int, default = 80) #输出字符画高

#获取参数
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output


def get_char(r, g, b, alpha = 256):
    # 判断alpha值
    if alpha == 0:
        return ''
    # 获取字符集的长度，这里为70
    length = len(ascii_char)
    # 将RGB转为灰度值gray，灰度值范围为0-255
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    # 灰度值范围为0-255，而字符集只有70
    # 需要进行如下处理才能将灰度值映射到指定的字符上
    unit = (256.0 + 1)/length
    # 返回灰度值对应的字符
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    IMG = r'ceshi.jpg'
    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'
    print(txt)

    # 字符画输出到文件
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open("out.txt", 'w') as f:
            f.write(txt)