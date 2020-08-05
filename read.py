from PIL import Image
import numpy as np
import string

im = Image.open('sample.jpg').convert('LA')
im = np.array(im)

#compress down to size
comp = 4
print(im.shape)

lim_x = im.shape[0]
lim_y = im.shape[1]

finish = ""


for i in range(0,lim_x,comp):
    for j in range(0,lim_y,comp):
        average_Color = np.sum(im[i:min(i+comp,lim_x),j:min(j+comp,lim_y),:]) / (2*comp * comp) 
        finish += chr(int(average_Color)) + ' '
    finish += '\n'

print(finish)

pil_img = Image.fromarray(im)
pil_img.save('newpic.png')
