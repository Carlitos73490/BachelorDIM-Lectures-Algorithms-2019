'''
a=1
b='e'+a
'''

'''//////////////////////////////////////////////////'''

def average_above_zero(table:list):
 '''
 This function return the average of a table given in parameters
 Args : 
     table : the list        
 Returns : the average of the list
 '''
 som = 0
 n = 0
 i = 0
 for i in range(len(table)):
     if len(table) > 0 :
         som = som + (table[i])
         n = n + 1
 return som/n
 
  
'''//////////////////////////////////////////////////'''


def max_value(table:list):
 '''
 This function return the max of a table given in parameters
 Args : 
     table : the list        
 Returns : the max value of the list
 '''
 vmax = 0
 for i in range(len(table)):
     if len(table) > 0 :
         if vmax < (table[i]):
             vmax = (table[i])
 return vmax
 
'''//////////////////////////////////////////////////'''

def reverse_table(table:list):
 '''
 This function return the reverese form of a table given in parameters
 Args : 
     table : the list        
 Returns :  value of the list
 '''
 i = 0
 j = len(table) - 1
 for i in range(int(j/2)):
     permut = table[i]
     table[i] = table[j]
     table[j] = permut
     i = i+1
     j= j-1
 return table

'''//////////////////////////////////////////////////'''
import numpy as np
def roi_bbox(input_image: np.array):
 '''
 This function return the reverese form of a table given in parameters
 Args : 
     table : the list        
 Returns   
 ''' 
 stop = 0
 '''coin haut gauche'''
 for i in range(len(input_image)):
  for j in range(len(input_image[0])):
      if input_image[i,j] > 0:
       CHG = i + 1, j+ 1
       stop = 1
       break
  if stop == 1:
   break

 stop = 0
   
 print("///////////////////")
 
 '''coin haut droit'''
 for i in range(len(input_image)):
  for j in reversed(range(len(input_image[0]))):
      if input_image[i,j] > 0:
       CHD = i + 1, j+ 1
       stop = 1
       break
  if stop == 1:
   break
 stop = 0
 print("///////////////////")
 
 '''coin bas droit'''
 for i in reversed(range(len(input_image))):
  for j in reversed(range(len(input_image[0]))):
      if input_image[i,j] > 0:
       CBD = i + 1, j+ 1
       stop = 1
       break
  if stop == 1:
   break
 stop = 0
       
 print("///////////////////")
 
 '''coin bas droit'''
 for i in reversed(range(len(input_image))):
  for j in range(len(input_image[0])):
      if input_image[i,j] > 0:
       CBG = i + 1, j+ 1 
       stop = 1
       break
  if stop == 1:
   break
 stop = 0

 print (CHG,CHD,CBG,CBD)
 
 bounding_box = 0
 if CHG[0] < CBD[0]:
  bounding_box = str(CHG) + " " + str(CBD)
  print(bounding_box)
 if CHG[0] > CBD[0]: 
  bounding_box = str(CHD) + " " + str(CBG)
  print(bounding_box)
  
  '''
      x1>x   x1 = 0
      y<y1   y1 =y
      x2 < x x2 = x
      y2 < y y2=y
  '''
    
 return input_image
 
  

maTable = [1,2,3,4,5,6,7,8,9,10,11,12,13]
'''print(reverse_table(maTable))'''
'''print(max_value(maTable))'''
'''print(average_above_zero(maTable))'''
H = 12
W = 10
monImage = np.zeros((H,W))
monImage[8:10,7:9] = np.ones((2,2))
monImage[2:4,3:5] = np.ones((2,2))*2

print(roi_bbox(monImage))

