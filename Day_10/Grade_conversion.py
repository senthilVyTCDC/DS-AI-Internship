Mark = int(input("Enter your Mark: "))
Mark = abs(Mark)
if Mark > 100:
    print("Enter the marks between 0-100:")
elif Mark > 90:
    print("Grade O")
elif Mark > 80:
    print("Grade A+")
elif Mark > 70:
    print("Grade A")
elif Mark > 60:
    print("Grade B+")
elif Mark > 50:
    print("Grade B")
elif Mark >= 45:
    print("Grade C")
else:
    print("Fail")
