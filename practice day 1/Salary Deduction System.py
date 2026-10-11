print("salary")
salary = float(input())
print("late days")
late_days = int(input())
print("absent day")
absent_days = int(input())

deduction = 0


if late_days > 10:
    deduction = deduction + 0.10
elif late_days > 5:
    deduction = deduction + 0.05


if absent_days > 2:
    deduction = deduction + 0.05


final_salary = salary - (salary * deduction)
print(int(final_salary))
