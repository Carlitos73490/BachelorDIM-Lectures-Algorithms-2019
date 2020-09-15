'''
a=1
b='e'+a
'''

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
 
  
maTable = [1,2,3,4,5,10]
print(average_above_zero(maTable))


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
 
  
maTable = [1,2,3,4,5,10]
print(max_value(maTable))

def reverse_table(table:list):
 '''
 This function return the reverese form of a table given in parameters
 Args : 
     table : the list        
 Returns : the max value of the list
 '''
 trie = false
 for i in range(len(table) - 1):
     print("test")
     if table[i] < table[i + 1]:
         table[i] = table[i + 1]
 return table
 
  
maTable = [1,2,3,4,5,10]
print(reverse_table(maTable))
