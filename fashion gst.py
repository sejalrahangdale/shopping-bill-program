def calculateFashionGST(c, d):
    total = c + d
    gst = total * 13 / 100
    return total + gst


c = 100
d = 100

result = calculateFashionGST(c, d)

print("Fashion Amount:", format(result, ".2f"))