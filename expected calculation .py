# def calculateElectronicsGST(a, b):
#     total = a + b
#     gst = total * 18 / 100
#     return total + gst



# fashion
# def calculateFashionGST(c, d):
#     total = c + d
#     gst = total * 13 / 100
#     return total + gst

# FOOD GST
# def calculateFoodGST(e):
#     gst = e * 7 / 100
#     return e + gst

# total after GST
# def totalBill(a, b, c, d, e):
#     electronics = calculateElectronicsGST(a, b)
#     fashion = calculateFashionGST(c, d)
#     food = calculateFoodGST(e)

#     total = electronics + fashion + food
#     return total

# 20% Calcuted discounted 
# Calculate 20% Discount on 569

def calculateDiscountedBill(total):
    discount = total * 20 / 100
    final_amount = total - discount
    return final_amount


# Total amount after GST
total = 569

# Calculate final payable amount
final_amount = calculateDiscountedBill(total)

# Calculate discount amount
discount = total - final_amount

# Display output
print("Total after GST:", format(total, ".2f"))
print("20% Discount:", format(discount, ".2f"))
print("Final payable amount:", format(final_amount, ".2f"))
