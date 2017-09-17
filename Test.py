def calculateOneYear (interest, price):
    return (1 + interest) * price

def calculateManyYears(numberYears, interest, valueToday) :
    valuePreviousYear = valueToday
    for x in range (0, numberYears):
        valuePreviousYear = calculateOneYear(interest, valuePreviousYear)
    return valuePreviousYear

print(calculateManyYears(40,0.025, 10))


