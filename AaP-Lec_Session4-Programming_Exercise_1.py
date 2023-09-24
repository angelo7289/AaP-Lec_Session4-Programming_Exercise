print("Enter your height: ")

Feet= int(input('Feet: '))
Inches= int(input('Inches '))
Inches += Feet*12
Height_cm=round(Inches*2.54, 1)
percentage = 0.88



result = Height_cm * percentage

print(result)
