def fun(words): 
   count=0    
   for word in words:      
      if len(word) >= 2 and word[0] == word[-1]: 
         count += 1    
         return count 
word_list = ['abc', 'xyz', 'aba', '1221', 'aa', 'ghg'] 
print("Number of matching words:", 
fun(word_list)) 
 
