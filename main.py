
# coding=utf-8
import PIL
import random
from PIL import Image
from PIL import ImageGrab
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageFilter


def make_ico(name,op1=False,op2=False,op3=False,op4=False,op5=False,op6=False,op7=False):
    s = name
    s = s.replace('\n','')
    s = s.replace(' ','')
    
    bg = Image.open("bg.png")
    bgr = bg.resize((120, 120), resample=Image.LANCZOS)
    bgr = bgr.crop(box=(0,12,120,108))

    fg = Image.open("assets/fg.png")
    bgr.paste(fg, (0, 0), mask=fg)
    #bgr.save("origin_ico.png")

    if op1:   
        s1 = Image.open("assets/upd.png")
        bgr.paste(s1, (4, 4), mask=s1)
    if op2:    
        s2 = Image.open("assets/vis.png")
        bgr.paste(s2, (92, 4), mask=s2)
    if op3:
        s3 = Image.open("assets/antispy.png")
        bgr.paste(s3, (4, 62), mask=s3)
    if op4:    
        s4 = Image.open("assets/amb.png")
        bgr.paste(s4, (92, 62), mask=s4)
    if op5:
        s5 = Image.open("assets/hero.png")
        bgr.paste(s5, (4, 62), mask=s5)        
   
    bgr.save("final.png")
    bgr = Image.open("final.png")
    draw = ImageDraw.Draw(bgr)
    font = ImageFont.truetype('fonts/zpix.ttf',18)

    sp = 120/(len(s)+1)
    for i in range(len(s)):
        draw.text((sp*(i+1)-4,76), s[i], font=font, fill="black")
        draw.text((sp*(i+1)-6,76), s[i], font=font, fill="white")

    fg2 = Image.open("assets/fg2.png")
    bgr.paste(fg2, (0, 0), mask=fg2)
    bgr.save("final.png")

    if op7: 
        bgr = Image.open("final.png")
        rd = Image.open("assets/ready.png")
        rd = rd.resize((60, 30), resample=0)
        bgr.paste(rd, (30, 0), mask=rd)
        bgr.save("final.png")
        
    if not op6: 
        bgr = Image.open("final.png")
        bgr = bgr.resize((60, 48), resample=0)
        bgr.save("final.png")



make_ico('老坛酸菜面',op1=True,op2=True,op3=True,op4=True,op5=True,op6=True,op7=True)

#打开
#image3 = Image.open("head3.png")

#重置大小
#imager = image.resize((1000, 200), resample=Image.LANCZOS)

#组合图片
#imager.paste(image2, (0, 0), mask=image2)

#保存图片
#imager.save("top3.png")

#绘制文字
#draw = ImageDraw.Draw(image4)
#font = ImageFont.truetype('kyokasho.ttf', 30)
#draw.text((190,90), '一只天上的大萝卜', font=font, fill=(192,64,128))

#绘制文字大小
#draw = ImageDraw.Draw(image4)
#font = ImageFont.truetype('kyokasho.ttf', 30)
#sizex = draw.textsize('一只天上的大萝卜')

#制图
#image5 = Image.new('RGB', (1000, 800), (255, 255, 255))

#裁切
#imagen = image5.crop(box=(0,0,18,20))

#画线
#draw = ImageDraw.Draw(image5)
#shape = [(50,250), (400,250)]
#draw.line(shape, fill=(128,128,128), width = 3)


