print("Adult Metric BMI")
print("Key>>>\nBMI Values")
print("Underweight: less than 18.5")
print("Normal: between 18.5 and 24.9")
print("Overweight: between 25 and 29.9")
print("Obese: 30 0r greater")
print(" ")
print(" ")
h_cm= float(input("Input height in cm: "))
w_kg= float(input("Input weight in kg: "))
h_msq= h_cm * 0.01
BMI = round(w_kg / (h_msq ** 2) , 2)
if ((BMI >= 100) or (BMI < 0)):
    print("Invalid Result")
elif ((BMI >= 0) and (BMI < 18.5)):
    print (BMI , "under weight")
elif ((BMI >= 18.5) and (BMI < 24.5)):
    print (BMI, "healthy weight")
elif ((BMI >= 25) and (BMI < 30)):
    print (BMI, "over weight")
elif ((BMI >= 30) and (BMI < 100)):
    print (BMI, "obese")
