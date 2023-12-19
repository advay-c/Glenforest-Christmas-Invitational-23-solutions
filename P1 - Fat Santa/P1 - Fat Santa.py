a, b, c = map(int, input().split())
stomachV = a**3
chocolateV = b * c**3
if stomachV >= chocolateV:
    print("Yes")
else:
    print("No")
