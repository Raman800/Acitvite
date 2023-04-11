'''
Complete the Following Exercises.

You are free to use any IDE.
Steps Involved:

1. Understand a Problem (Make it clear through Instructor)

2. Understand Inputs

3. Understand Output 

4.Understand the Constraints

5.Code 

6. Validate  

 

            Arithmetic: Input some numbers, do some simple arithmetic, output results (Python3)
            Conversion: Input some numbers, do some simple arithmetic to do silly conversions(Python3) 
            Earthquake Impact: Input some numbers, do some simple arithmetic, output results. (Python3)
            Factor:  Calculate temperature that a person feels because of the wind (Python3)

'''
#Arthemetic 
y=float(input("first number (y):"))
z=float(input("second number(z):"))

add=y+z
print("addition: ",add)
sub=y-z
print("Substraction: ",sub)
multiple=y*z
print("multiple: ",multiple)
divide=y/z
print("division: ",divide)
power=y**z
print("power: ",power)
floor_division= (y//z)
print("floor division: ",floor_division)
Modulo=y%z
print("Modulo: ",Modulo)


#Conversion
meter=float(input("enter value in meter: "))
n=input("convert meter in: ")
if n=="centimeter":
    print(meter*0.01)
elif n=="millimeter":
    print(meter*0.001)
elif n=="nanometer":
    print(meter*(10**9))
elif n=="kilometer":
    print(meter*1000)
elif n=="hectometer":
     print(meter*100)


#Earthquake impact
speed_of_waves=float(input("Enter speed: km/h"))

if speed_of_waves< 2:
    impact = "No imapct, but recorded"
elif speed_of_waves >= 2 and speed_of_waves < 4:
    impact = "Felt, by few people"
elif speed_of_waves  >= 4 and speed_of_waves < 6:
    impact = "Felt by people, but no damage."
elif speed_of_waves  >= 6 and speed_of_waves <  7:
    impact = "Light damage."
elif speed_of_waves  >= 7 and speed_of_waves < 8:
    impact = "Moderate damage."
elif speed_of_waves  >= 8 and speed_of_waves <10:
    impact = "Severe damage."
elif speed_of_waves  >= 10 and speed_of_waves < 13:
    impact = "Major earthquake."
else:
    impact = "Great earthquake, can have more and more destruction."

print("speed:", speed_of_waves)
print("Impact:", impact)


#Factor
temp = float(input("Enter air temperature in degrees Celsius: "))
wind_speed_temp = float(input("Enter wind speed in kilometers per hour: "))

wind_chill_temp = 13.12 + 0.6215 * temp - 11.37 * (wind_speed_temp ** 0.16) + 0.3965 * temp * (wind_speed_temp** 0.16)

print("Wind chill temperature:", wind_chill_temp, "degrees Celsius")