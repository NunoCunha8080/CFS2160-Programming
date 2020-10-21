import math
'''Task5'''
print("Temperature Converter\n")
print("To which temperature you wish to convert to?\n")
print("Press (f) for Fahrenheit or (c) for Celsius\n")
T_Choice = None

while T_Choice not in ("f", "c"):
    T_choice = str(input())
    if T_choice == "f":
        T_Celsius = float(input("Insert the Celsius temperature you wish to convert\n"))
        T_Result = T_Celsius*(9/5)+32
        T_Result = round(T_Result, 1)
        print(str(T_Celsius)+" degrees Celsius is "+str(T_Result)+" Fahrenheit")
        quit()
    elif T_choice == "c":
        T_Fahrenheit = float(input("Insert the Fahrenheit temperature you wish to convert\n"))
        T_Result = (T_Fahrenheit-32)*(5/9)
        T_Result = round(T_Result, 1)
        print(str(T_Fahrenheit) + " degrees Fahrenheit is " + str(T_Result) + " Celsius")
        quit()
    else:
        print("Please select one of the 2 options\n")
        print("To which temperature you wish to convert to?\n")
        print("Press (f) for Fahrenheit or (c) for Celsius\n")