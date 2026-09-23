








salary = int(input("Enter your salary per month:"))
if 500<salary or salary<0:
    print("Invalid salary! try again.")
elif 450<salary<=500:
        tax = salary * 0.4
        income = salary - tax
        print("tax:", tax, "/", "income:", income)
elif 400<salary<=450:
        tax = salary * 0.35
        income = salary - tax
        print("tax:", tax, "/" "income:" , income)
elif 350<salary<=400:
        tax = salary * 0.3
        income = salary - tax
        print("tax:", tax, "/" "income:", income)
elif 300<salary<=350:
        tax = salary * 0.25
        income = salary - tax
        print("tax:", tax, "/", "income:", income)
elif 250<salary<=300:
        tax = salary * 0.2
        income = salary - tax
        print("tax:", tax, "/", "income:", income)
elif 200<salary<=250:
        tax = salary * 0.15
        income = salary - tax
        print("tax:", tax, "/", "income:", income)
elif 150<salary<=200:
        tax = salary * 0.13
        income = salary - tax
        print("tax:", tax, "/", "income:", income)
elif 100<salary<=150:
        tax = salary * 0.11
        income = salary - tax
        print("tax:", tax, "/", "income:", income)
elif 50<salary<=100:
        tax = salary * 0.09
        income = salary - tax
        print("tax:", tax, "/", "income:", income)
else:
    if salary<=50:
        print("No tax is deducted.")
