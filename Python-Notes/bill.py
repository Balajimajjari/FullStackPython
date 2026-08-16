units=int(input())
senior=input()
if 0 < units <= 100:
    bill = units * 1.5
elif 101 < units <= 200:
    bill = units * 2.5
elif 201 < units <= 500:
    bill = units * 4
else:
    bill = units * 6
if senior == "True":
    bill = bill * 0.9
if units > 800:
    bill = bill * 1.05
print(int(bill))
