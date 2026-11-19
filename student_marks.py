name = input("Enter student name: ")

m1 = int(input("Enter marks in Subject 1: "))
m2 = int(input("Enter marks in Subject 2: "))
m3 = int(input("Enter marks in Subject 3: "))

total = m1 + m2 + m3
average = total / 3

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)

PASS_MARK = 35

if average >= PASS_MARK:
    print("Result: PASS")
else:
    print("Result: FAIL")