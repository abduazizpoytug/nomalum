boshlash = input('boshlashni hohlaysizmi: ')

if boshlash == "yoq":
    print("hop oyin tugadi")
    
    
while boshlash == 'ha':
    num = int(input('sonni kiriting: '))
    num2 = int(input('ikkinchi sonni kiriting: '))
    value = input("amalni kiriting: ")
    if value == "+":
        print("natija: " + str(num + num2))
    elif value == "-":
        print("natija: " + str(num - num2))
    elif value == "*":
        print("natija: " + str(num * num2))
    elif value == "/":
        print("natija: " + str(num / num2))
        
    boshlash = input('qayta boshlash hohlaysizmi: ').lower()