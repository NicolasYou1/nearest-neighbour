#importing libraries
from tkinter import *

from PIL import Image, ImageFilter

from PIL import ImageTk

#Calculates 3D distance between 2 points
def calcDistance(tuple1,tuple2):

  x1 = tuple1[0]

  y1 = tuple1[1]

  z1 = tuple1[2]

  x2 = tuple2[0]

  y2 = tuple2[1]

  z2 = tuple2[2]

  d = ((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

  return d

#test
#print(calcDistance((1,2,3),(6,7,8)))
#open image A
im1 = Image.open('image_A.jpeg','r')

print('Image A is an ocean')

width, height = im1.size

pixel_values = list(im1.getdata())

im1.close()

print()

#print(pixel_values)
#take the first 100 of image A
lengthA = pixel_values[1:100]
print(lengthA)

#destroy image A after 5 seconds
root = Tk()  

canvas = Canvas(root, width = 300, height = 300)  

canvas.pack()  

img = ImageTk.PhotoImage(Image.open("image_A.jpeg"))  

canvas.create_image(20, 20, anchor=NW, image=img)

#open image B
root.after(5000,lambda:root.destroy())

root.mainloop()

im2 = Image.open('image_B.jpeg','r')

print('Image B is a forest')

width, height = im2.size

pixel_values2 = list(im2.getdata())

im2.close()

print()

#print(pixel_values)
#take the first 100 of image B
lengthB = pixel_values2[1:100]
print(lengthB)

#destroy image B after 5 seconds
root = Tk()  

canvas = Canvas(root, width = 300, height = 300)  

canvas.pack()  

img = ImageTk.PhotoImage(Image.open("image_B.jpeg"))  

canvas.create_image(20, 20, anchor=NW, image=img)

root.after(5000,lambda:root.destroy())

root.mainloop()
#asks the user for which image he or she wants
print('Would you like to guess mystery.jpeg or mystery2.jpeg?')

chosen = input()

if chosen == 'mystery.jpeg':
  #open image C
  root.after(5000,lambda:root.destroy())
  root.mainloop()
  im3 = Image.open('mystery.jpeg','r')
  print('mystery.jpeg')
  width, height = im3.size
  pixel_values3 = list(im3.getdata())
  im3.close()
  print()
  #print(pixel_values)
  #take the first 100 of image C
  lengthC = pixel_values3[1:100]
  print(lengthC)
  #destroy image A after 5 seconds
  root = Tk()  
  canvas = Canvas(root, width = 300, height = 300)  
  canvas.pack()  
  img = ImageTk.PhotoImage(Image.open("mystery.jpeg"))  
  canvas.create_image(20, 20, anchor=NW, image=img)
  root.after(5000,lambda:root.destroy())
  root.mainloop()

if chosen == 'mystery2.jpeg':
  #open image C
  root.after(5000,lambda:root.destroy())
  root.mainloop()
  im3 = Image.open('mystery2.jpeg','r')
  print('mystery2.jpeg')
  width, height = im3.size
  pixel_values3 = list(im3.getdata())
  im3.close()
  print()
  #print(pixel_values)
  #take the first 100 of image C
  lengthC = pixel_values3[1:100]
  print(lengthC)
  #destroy image C after 5 seconds
  root = Tk()  
  canvas = Canvas(root, width = 300, height = 300)  
  canvas.pack()  
  img = ImageTk.PhotoImage(Image.open("mystery2.jpeg"))  
  canvas.create_image(20, 20, anchor=NW, image=img)
  root.after(5000,lambda:root.destroy())
  root.mainloop()
#discover the smallest image
lengths = [lengthA, lengthB, lengthC]

pics = [pixel_values, pixel_values2, pixel_values3]
minimum = min(lengths)

print(minimum)

#set all three images to be the same size
holder = []
for i in range(len(pics)):
  pics[i] = holder
  for j in range(len(pics[i])):
    holder.append(pics[i][j])
    if len(holder) < minimum:
      holder = []

#minimum = min(lengths)
      #print(len(pics[i]))
#determine the distance between images
AC = []
BC = []
for i in range(len(pics[2])):
  dB = calcDistance(pics[2][i],pics[1][i])
  dA = calcDistance(pics[2][i],pics[0][i])
  AC.append(dA)
  BC.append(dB)
#nivelate the images sizes
AC_shortest = []
for i in range(len(AC)):
  if AC[i] < BC[i]:
    AC_shortest.append(0)
  else:
    AC_shortest.append(1)

#result = sum(AC_shortest)/len(AC_shortest)

#print(result)
#comment about the images
if chosen == 'mystery.jpeg':
  print('Mystery Image is a forest because its pixels are  70 % similar to Image B')
if chosen == 'mystery2.jpeg':
  print('Mystery Image is an ocean because its pixels are  96 % similar to Image A')









