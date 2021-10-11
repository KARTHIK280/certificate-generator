#certificate
from PIL import Image , ImageDraw , ImageFont
import pandas as pd
import xlrd

df = pd.read_excel("Book.xlsx")
for index,j in df.iterrows():
    img = Image.open('template.jpeg')
    draw = ImageDraw.Draw(img)
    draw.text(xy=(450,320),text ='{}'.format(j['Name']),fill =(0,137,209),font = ImageFont.truetype('arial.ttf',120))
    draw.text(xy=(290,580),text ='{}'.format(j['Project Name']),fill =(0,0,102),font = ImageFont.truetype('arial.ttf',120))
    draw.text(xy=(140,880),text ='{}'.format(j['Mentor Name']),fill =(102,0,51),font = ImageFont.truetype('arial.ttf',50))
    draw.text(xy=(1100,880),text ='{}'.format(j['Project Manager']),fill =(102,0,51),font = ImageFont.truetype('arial.ttf',50))
    draw.text(xy=(750,900),text ='{}'.format(j['Certificate Number']),fill =(102,0,51),font = ImageFont.truetype('arial.ttf',30))
    img.save('certificates\{}.jpeg'.format(j['Name']))
print('CERTIFICATE GENERATED SUCCESSFULLY !!')
   