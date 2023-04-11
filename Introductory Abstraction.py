'''
Complete the Exercises - Representing Abstraction Through Code 
In programming, we deal with two kinds of elements: functions and data. 

Informally, data is stuff that we want to manipulate, and functions describe the rules for manipulating the data. 

By the concept of abstraction create functions representing abstracting principles through function 

Think and design a user-defined function that should provide the result by mare passing few arguments by the calling function.
Arithmetic: Input some numbers, do some simple arithmetic, output results (Python3)
Conversion: Input some numbers, do some simple arithmetic to do silly conversions(Python3) 
Earthquake Impact: Input some numbers, do some simple arithmetic, output results. (Python3)
Factor:  Calculate temperature that a person feels because of the wind (Python3)
Note: Naming Convention Files: Crate files based on the purpose of the exercise eg: If calculating factor then use function_factor.py  Submission Guidelines: File Upload (Notepad File, Python File, Console Output Pasted) 
'''


#Arithmetic
def do_arithmetic(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    modulus = a % b

    return addition, subtraction, multiplication, division, modulus



#Conversion
def do_conversion(num, unit, target_unit):
    # conversion factors for various units
    if unit == "feet":
        factor = 0.3048
    elif unit == "miles":
        factor = 1609.34
    elif unit == "inches":
        factor = 0.0254

    converted_num = num * factor

    return f"{num} {unit} is equal to {converted_num} {target_unit}"




#Earthquake Impact
def calculate_earthquake_impact(magnitude):
    impact = 10**(1.5*magnitude - 5.75)
    return f"The potential impact of the earthquake is {impact}"




#Factor
import math
def calculate_wind_chill_factor(wind_speed, temperature):
    # formula to calculate wind chill factor
    factor = 35.74 + 0.6215*temperature - 35.75*math.pow(wind_speed, 0.16) + 0.4275*temperature*math.pow(wind_speed, 0.16)

    return f"The wind chill factor is {factor} degrees Fahrenheit."