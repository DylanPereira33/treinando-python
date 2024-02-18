strings = ["ab","ab","abc"]
queries = ["ab","abc","bc"]

 


list = []
for i in queries:
      cont = 0
      for num in strings:
         if i == num:
             cont +=1 
      list.append(cont)
print(list)
