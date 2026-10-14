# Q3: Calculate Food GST

def calculateFoodGST(e):
    gst = e * 7 / 100
    total = e + gst
    return total


# Sample test values
a = 100
b = 100
c = 100
d = 100
e = 100

# Function call using the sample value directly
result = calculateFoodGST(e)

# Display output
print("Food Amount:", format(result, ".2f"))