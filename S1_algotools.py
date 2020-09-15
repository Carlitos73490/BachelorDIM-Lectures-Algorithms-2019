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
 
  

maTable = [1,2,3,4,5,6,7,8,9,10,11,12,13]
'''print(max_value(maTable))'''
'''print(average_above_zero(maTable))'''
print(reverse_table(maTable))
