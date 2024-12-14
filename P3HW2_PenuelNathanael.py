# Nathanael Penuel
# 10/27/2024
# P3HW2 - Salary Calculator
# This program calculates the regular, overtime, and gross pay for an employee.

# 1. Start
# 2. Input name
# 3. Input number of hours worked
# 4. Input pay rate
# 5. If hours worked > 40:
#    a. Calculate overtime hours = hours worked - 40
#    b. Calculate overtime pay = overtime hours * (pay rate * 1.5)
#    c. Calculate regular pay = 40 * pay rate
# 6. Else:
#    a. Overtime hours = 0
#    b. Overtime pay = 0
#    c. Regular pay = hours worked * pay rate
# 7. Calculate gross pay = regular pay + overtime pay
# 8. Display name, hours worked, pay rate, overtime hours, overtime pay, regular pay, and gross pay
# 9. End

# Get input from the user
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Start values
overtime_hours = 0
overtime_pay = 0
regular_pay = 0

# Check if employee worked overtime
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = 40 * pay_rate
else:
    regular_pay = hours_worked * pay_rate

# Calculate gross pay
gross_pay = regular_pay + overtime_pay

# Display results
print("--------------------------------------------")
print("Employee name: ", employee_name)
print("--------------------------------------------")
print("Hours Worked:   ", hours_worked)
print("Pay Rate:       ", pay_rate)
print("Overtime Hours: ", overtime_hours)
print("Overtime Pay:   ", round(overtime_pay, 2))
print("Regular Pay:    ", round(regular_pay, 2))
print("Gross Pay:      ", round(gross_pay, 2))
