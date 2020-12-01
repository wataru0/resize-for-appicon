# アプリアイコン用画像リサイズ
from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-source",type=str)
parser.add_argument("-size",type=int)


def main():
    args = parser.parse_args()
    im = Image.open('./pic/'+args.source)
    img_resize = im.resize((args.size,args.size))
    img_resize.save('./pic/'+str(args.size)+'.png')


if __name__ =='__main__' :
    main()