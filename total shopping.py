def calculateElectronicsGST(a, b):
    total = a + b
    gst = total * 18 / 100
    return total + gst


def calculateFashionGST(c, d):
    total = c + d
    gst = total * 13 / 100
    return total + gst


def calculateFoodGST(e):
    gst = e * 7 / 100
    return e + gst


def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)

    total = electronics + fashion + food
    return total


a = 100
b = 100
c = 100
d = 100
e = 100

result = totalBill(a, b, c, d, e)

print("Total Shopping Bill:", format(result, ".2f"))