def calculateFoodGST(e):
    gst = e * 7 / 100
    return e + gst


e = 100

result = calculateFoodGST(e)

print("Food Amount:", format(result, ".2f"))