from PIL import Image, ImageDraw, ImageColor
import numpy as np
import time
import os


def demo():
    im = Image.new("RGB", (100, 100), (255, 255, 255))
    drawObject = ImageDraw.Draw(im)
    drawObject.line([50, 50, 80, 80], fill="yellow", width=5)
    drawObject.rectangle([10, 10, 40, 40], fill="green")
    drawObject.arc([50, 10, 80, 40], 0, 90, fill="red")
    drawObject.pieslice((20, 20, 60, 60), 0, 90, fill="blue")
    drawObject.ellipse((50, 50, 70, 80), fill="black")
    drawObject.polygon([(20, 20), (60, 30), (30, 60)], outline="red")
    drawObject.polygon([(20, 20), (30, 25), (35, 50)], fill="yellow")
    drawObject.chord((50, 50, 60, 60), 0, 90, outline="red")
    # im.save("xxx.jpg")
    pass


# 新建目录
def make_dir_if_noe_exist(sample_dir):
    if not os.path.exists(sample_dir):
        os.makedirs(sample_dir)
    pass


# 画圆
def paint_cycle(name, radius, size, color="black", bg_color="white"):
    im = Image.new("RGB", (size, size), bg_color)
    draw = ImageDraw.Draw(im)
    draw.ellipse((size//2 - radius, size//2 - radius, size//2 + radius, size//2 + radius), fill=color)
    im.save(name)
    pass


def generator_cycles(number, dir, size):
    make_dir_if_noe_exist(dir)
    for i in range(number):
        radius = np.random.randint(1, size//2)
        paint_cycle(dir + str(i) + "_" + str(radius) + "_c.jpg", radius=radius, size=size)
    pass


# 矩形
def paint_rectangle(name, xy, size, color="black", bg_color="white"):
    im = Image.new("RGB", (size, size), bg_color)
    draw = ImageDraw.Draw(im)
    draw.rectangle((size//2 - xy[0], size//2 - xy[1], size//2 + xy[0], size//2 + xy[1]), fill=color)
    im.save(name)
    pass


def generator_rectangle(number, dir, size):
    make_dir_if_noe_exist(dir)
    for i in range(number):
        xy = (np.random.randint(1, size//2), np.random.randint(1, size//2))
        paint_rectangle(dir + str(i) + "_" + str(xy[0]) + "_r.jpg", xy=xy, size=size)
    pass


# 正方形
def paint_square(name, x, size, color="black", bg_color="white"):
    im = Image.new("RGB", (size, size), bg_color)
    draw = ImageDraw.Draw(im)
    draw.rectangle((size//2 - x, size//2 - x, size//2 + x, size//2 + x), fill=color)
    im.save(name)
    pass


def generator_square(number, dir, size):
    make_dir_if_noe_exist(dir)
    for i in range(number):
        x = np.random.randint(1, size//2)
        paint_square(dir + str(i) + "_" + str(x) + "_s.jpg", x=x, size=size)
    pass


# 三角形
def paint_triangle(name, abc, size, color="black", bg_color="white"):
    im = Image.new("RGB", (size, size), bg_color)
    draw = ImageDraw.Draw(im)
    tem_1 = (2 * abc[0], size//2 - abc[1])
    tem_2 = (2 * abc[2], size//2 + abc[3])
    tem_3 = (size - (tem_1[0] + tem_2[0])//2, size - (tem_1[1] + tem_2[1])//2)
    draw.polygon([tem_1, tem_2, tem_3], fill=color)
    im.save(name)
    pass


def generator_triangle(number, dir, size):
    make_dir_if_noe_exist(dir)
    for i in range(number):
        abc = (np.random.randint(1, size//2), np.random.randint(1, size//2),
               np.random.randint(1, size//2), np.random.randint(1, size//2))
        paint_triangle(dir + str(i) + "_" + str(abc[0]) + "_t.jpg", abc=abc, size=size)
    pass


# 椭圆
def paint_ellipse(name, xy, size, color="black", bg_color="white"):
    im = Image.new("RGB", (size, size), bg_color)
    draw = ImageDraw.Draw(im)
    draw.ellipse((size // 2 - xy[0], size // 2 - xy[1], size // 2 + xy[0], size // 2 + xy[1]), fill=color)
    im.save(name)
    pass


def generator_ellipse(number, dir, size):
    make_dir_if_noe_exist(dir)
    for i in range(number):
        xy = (np.random.randint(1, size // 2), np.random.randint(1, size // 2))
        paint_ellipse(dir + str(i) + "_" + str(xy[0]) + "_e.jpg", xy=xy, size=size)
    pass


# 生成所有的图形
def generator_all(path, num=100, size=128):

    start = time.clock()
    generator_cycles(num, path, size)
    print(time.clock() - start)

    start = time.clock()
    generator_rectangle(num, path, size)
    print(time.clock() - start)

    start = time.clock()
    generator_triangle(num, path, size)
    print(time.clock() - start)

    start = time.clock()
    generator_ellipse(num, path, size)
    print(time.clock() - start)

    start = time.clock()
    generator_square(num, path, size)
    print(time.clock() - start)

    pass


def samples():
    generator_cycles(100, "img/cycle/", 128)
    generator_rectangle(100, "img/rectangle/", 128)
    generator_triangle(100, "img/triangle/", 128)
    generator_ellipse(100, "img/ellipse/", 128)
    generator_square(100, "img/square/", 128)
    pass

if __name__ == "__main__":

    # generator_all("img/all/", 100)

    pass
