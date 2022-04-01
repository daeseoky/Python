input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
result = 0

if row + 2 <= 8:
   if column + 1 <= 8:
       result += 1
   if column - 1 >= 1:
       result += 1

if row + 1 <= 8:
   if column + 2 <= 8:
       result += 1
   if column - 2 >= 1:
       result += 1

if row - 2 >= 1:
   if column + 1 <= 8:
       result += 1
   if column - 1 >= 1:
       result += 1

if row - 1 >= 1:
   if column + 2 <= 8:
       result += 1
   if column - 2 >= 1:
       result += 1

print(result)