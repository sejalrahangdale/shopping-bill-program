def calculateElectronicsGST(a, b):
    total = a + b
    gst = total * 18 / 100
    return total + gst


a = 100
b = 100

result = calculateElectronicsGST(a, b)

print("Electronics Amount:", format(result, ".2f"))