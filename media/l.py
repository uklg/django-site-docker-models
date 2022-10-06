#!/usr/bin/python3

from PIL import Image, ImageFont, ImageDraw

new = Image.new(mode="RGBA", size=(760,80))


draw = ImageDraw.Draw(new) 

#font = ImageFont.load_default().font

font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 64, encoding="unic")
font2 = ImageFont.truetype("MUSICELE.TTF", 64, encoding="unic")


#help(ImageFont.truetype)



text = 'Saturday Night DJ'
xoffset= 672
font2 = ImageFont.truetype("MUSICELE.TTF", 64, encoding="unic")



text2 = 'r'
text2='f'
text2='r'


draw.text((0, 0), text, font=font, align ="left")
draw.text((1, 1), text, font=font, align ="left",fill=(255,0,0,255))
draw.text((2, 2), text, font=font, align ="left",fill=(255,255,0,255))
draw.text((3, 3), text, font=font, align ="left",fill=(255,255,255,255))


draw.text((xoffset, 0), text2, font=font2, align ="left")
draw.text((xoffset+1, 1 ), text2, font=font2, align ="left",fill=(255,0,0,255))
draw.text((xoffset+2, 2 ), text2, font=font2, align ="left",fill=(255,255,0,255))
draw.text((xoffset+3, 3 ), text2, font=font2, align ="left",fill=(255,255,255,255))






new.show()

new.save('this.png')
