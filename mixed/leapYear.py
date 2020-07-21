year= -400

if ((year%4 == 0 and year%100 != 0) or year%400==0) and year>0:
    print("Leap year")
else:
    print("Not leap year")