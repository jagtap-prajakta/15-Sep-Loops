# WAP to calculate the average of a given list 

list = [10, 20, 30, 50, 50]
sum = 0
for num in list:
    sum = sum + num
    average = sum / len(list)
print("The average of the given list is: ", average)

