print(''' 
1 for add
2 for sub
3 for multi
4 for div
''')
num1 = input("enter the first number: ")  #num1 k nam ka variable banao
num2 = input("enter the second number: ")  #num2 ka variable banao
opr = input("enter the operator.. ")  #user pe operator lo
if opr == "1":  #agar 1 k equal h toh add hoga
  print(int(num1) + int(num2))
elif opr == "2":  #agar 2 k equal h toh sub hoga
  print(int(num1) - int(num2))
elif opr == "3":  #agar e k equal hoga toh multi
  print(int(num1) * int(num2))
elif opr == "4":  #agar 4 k equal hoga toh dev
  print(int(num1) / int(num2))
else:
  print("invalid opr...")  # agar or koi key press kie toh invalid operator
