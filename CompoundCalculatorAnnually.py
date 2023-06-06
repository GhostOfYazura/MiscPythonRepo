import time

def CalculateAndDisplay(remainingCycles = 365, amount = 1.0):
    while remainingCycles > 1:
        amount += amount * ((6/365)/100)
        print(amount * ((6/365)/100))
        print(str(remainingCycles) + " left current total is: " + str(round(amount, 2)))
        remainingCycles-=1
    return amount

    if remainingCycles < 1:
        return amount
    elif remainingCycles > 0:
        amount += amount * ((6/365)/100)
        print(amount * ((6/365)/100))
        print(str(remainingCycles) + " left current total is: " + str(round(amount, 2)))
        CalculateAndDisplay(remainingCycles-1, amount)
        return 10.0

def years(yearsRemaining = 30, yearlyTotal = 1.0):
    if yearsRemaining < 1:
        return
    else:
        yearlyTotal = CalculateAndDisplay(365, yearlyTotal)
        print(yearlyTotal)
        #time.sleep(3)
        years(yearsRemaining-1, yearlyTotal)

#CalculateAndDisplay(365, 10000)
years(30, 10000.0)