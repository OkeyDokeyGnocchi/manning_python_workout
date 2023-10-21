# Summing Numbers
# Create a mysum() function that sums given numbers
#  - Should allow arbitrary number of inputs using * splat

def mysum(numbers, start=0):
    total = start
    for number in numbers:
        total += number
    return total

# Testing
print("### Testing mysum function ###")
print(mysum([1,2]))
print(mysum([5,15,10]))
print(mysum([100,100,100,100,100,100,100,100,100,100]))
print(mysum([1, -2]))

# Testing after adding start variable
print(mysum([1,2,3], 4))

def myaverage(*numbers):
    total = 0
    count = 0
    for number in numbers:
        total += number
        count += 1
    average = total/count

    return average

# Testing myaverage
print(myaverage(10, 10))
print(myaverage(5, 10, 12))
print(myaverage(1,2,4))