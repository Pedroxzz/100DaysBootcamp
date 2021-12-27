height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight/(height ** 2))

if bmi <= 18.5:
    print("Your BMI is {}, you are underweight.".format(bmi))
elif bmi <= 25:
    print("Your BMI is {}, you have a normal weight.".format(bmi))
elif bmi <= 30:
    print("Your BMI is {}, you are slightly overweight".format(bmi))
elif bmi <= 35:
    print("Your BMI is {}, you are obese".format(bmi))
elif bmi > 35:
    print("You are clinically obese.")