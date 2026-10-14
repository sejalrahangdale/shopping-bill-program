# Task 01: Shopping Bill - GST First, Discount After

# Q1: Calculate Electronics GST (18%)
def calculateElectronicsGST(a, b):
    total = a + b
    gst = total * 18 / 100
    return total + gst


# Q2: Calculate Fashion GST (13%)
def calculateFashionGST(c, d):
    total = c + d
    gst = total * 13 / 100
    return total + gst


# Q3: Calculate Food GST (7%)
def calculateFoodGST(e):
    gst = e * 7 / 100
    return e + gst


# Q4: Calculate Total Bill
def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)

    total = electronics + fashion + food
    return total


# Q5: Calculate Discounted Bill
def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100
    final_amount = total - discount

    return final_amount


# Main program
# Sample test values supplied directly
a = 100
b = 100
c = 100
d = 100
e = 100

# Calculate amounts
electronics = calculateElectronicsGST(a, b)
fashion = calculateFashionGST(c, d)
food = calculateFoodGST(e)

total = totalBill(a, b, c, d, e)
final_amount = calculateDiscountedBill(a, b, c, d, e)

discount = total - final_amount

# Display results
print("Electronics Amount:", format(electronics, ".2f"))
print("Fashion Amount:", format(fashion, ".2f"))
print("Food Amount:", format(food, ".2f"))
print("Total after GST:", format(total, ".2f"))
print("Discount:", format(discount, ".2f"))
print("Final payable amount:", format(final_amount, ".2f"))