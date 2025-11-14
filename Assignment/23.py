string = input("Enter a string: ") 
 
if len(string) < 2:     
        result = "Empty String"
else:    
       result = string[:2] + string[-2:] 
 
print("Resulting string:", result) 
 
