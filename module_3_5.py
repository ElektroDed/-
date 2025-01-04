def get_multiplied_digits(numbers):
 str_number = str(numbers)
 first = int(str_number[0])

 if len(str_number) <= 1 :
     
   if str_number != '0':
        return first
    
   else:
         return 1

 else:
     return first * get_multiplied_digits(int(str_number[1:]))

result1 = get_multiplied_digits(50203040)
print(result1)
result2 = get_multiplied_digits(5020304)
print(result2)
