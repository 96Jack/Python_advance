from PIL import Image
import sys

TARGET_WIDTH = 300
CHAR = ['a','s','e', 'r', 'f', 'l', 'i', 's', 'c', 'm', '=' ]

def resize_img(img):
    w, h = img.size
    target_h = int(TARGET_WIDTH * h/float(w) * 0.5)
    new_img = img.resize((TARGET_WIDTH, target_h))
    return new_img

def gen_new_pixels(pixels):
    new_pixels = []
    
    for pixel in pixels:
        index = pixel // 25
        new_pixels.append(CHAR[index])

    return "".join(new_pixels)

if __name__ == "__main__":
    img_path = sys.argv[1]
    img = Image.open(img_path)
    img = resize_img(img=img)
    gray_img = img.convert('L')
    # gray_img.show()
    pixels = gray_img.getdata()
    new_pixels = gen_new_pixels(pixels)

    char_img = [new_pixels[index: index+TARGET_WIDTH] 
                for index in range(0, len(new_pixels), TARGET_WIDTH)]

    # print('\n'.join(char_img))
    with open("./char.txt",'w') as fp:
        fp.write('\n'.join(char_img))
