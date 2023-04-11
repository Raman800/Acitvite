'''
Problem -I 

The wavelength of visible light ranges from 380 to 750 nanometers (nm). While the
spectrum is continuous, it is often divided into 6 colors as shown below:

Violet 380 to less than 450
Blue 450 to less than 495
Green 495 to less than 570
Yellow 570 to less than 590
Orange 590 to less than 620
Red 620 to 750

Write a program that reads a wavelength from the user and reports its color. Display
an appropriate error message if the wavelength entered by the user is outside of the
visible spectrum.
'''

wavelength = float(input("Enter wavelength in nanometers (nm): "))

if wavelength < 380 or wavelength > 750:
    print("Error: Wavelength is outside of the visible spectrum!")
else:
    if 380 <= wavelength < 450:
        color = "Violet"
    elif 450 <= wavelength < 495:
        color = "Blue"
    elif 495 <= wavelength < 570:
        color = "Green"
    elif 570 <= wavelength < 590:
        color = "Yellow"
    elif 590 <= wavelength < 620:
        color = "Orange"
    else: 
        color = "Red"

    print(f"The color corresponding to {wavelength} nm is {color}.")

    
'''
Problem -II

Electromagnetic radiation can be classified into one of 7 categories according to its
frequency, as shown in the table below:

Radio Waves Less than 3 × 10^9
Microwaves 3 × 10^9 to less than 3 × 10^12
Infrared Light 3 × 10^12 to less than 4.3 × 10^14
Visible Light 4.3 × 10^14 to less than 7.5 × 10^14
Ultraviolet Light 7.5 × 10^14 to less than 3 × 10^17
X-Rays 3 × 10^17 to less than 3 × 10^19
Gamma Rays 3 × 10^19 or more

Write a program that reads the frequency of some radiation from the user and
displays name of the radiation as part of an appropriate message.
'''
frequency = float(input("Enter frequency in Hertz (Hz): "))

if frequency < 3e9:
    category = "Radio Waves"
elif 3e9 <= frequency < 3e12:
    category = "Microwaves"
elif 3e12 <= frequency < 4.3e14:
    category = "Infrared Light"
elif 4.3e14 <= frequency < 7.5e14:
    category = "Visible Light"
elif 7.5e14 <= frequency < 3e17:
    category = "Ultraviolet Light"
elif 3e17 <= frequency < 3e19:
    category = "X-Rays"
else:
    category = "Gamma Rays"
    
print(f"A frequency of {frequency} Hz corresponds to {category}.")
