height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = round(weight / height ** 2, 1)
if bmi < 18.5:
    status = "Underweight"
elif 18.5 <= bmi < 25:
    status = "Healthy Weight"
elif 25 <= bmi < 30:
    status = "Overweight"
else:
    status = "Obese"
print(f"BMI: {bmi}")
print(f"Status: {status}")
