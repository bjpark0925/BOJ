grade_table = {'A+':4.5, 'A0': 4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
credit_sum = 0
overall = 0
for i in range(20):
    subject, credit, grade = input().split()
    credit = float(credit)
    if grade in grade_table:
        credit_sum += credit
        overall += credit * grade_table[grade]

print("{:.6f}".format(overall/credit_sum))