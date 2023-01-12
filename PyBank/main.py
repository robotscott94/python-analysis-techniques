# read csv file
import os
import csv

bankData = os.path.join("Resources", "budget_data.csv")

# Create array of profit data
with open(bankData) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader, None)

    values = [float(row[1]) for row in csvreader]
    
# Create correspoding array of month data
with open(bankData) as csvfile:   
    csvreader2 = csv.reader(csvfile, delimiter=',')

    next(csvreader2, None)

    months = [row[0] for row in csvreader2]

# Calculate number of months
    
rowcount = len(values)  

# Calculate net profit
netprofit = 0
for i in range(len(values)):
    netprofit += values[i]


# Calculate average change
total_change = 0
for i in range(1, len(values)):
    total_change += values[i] - values[i - 1]
        
average_change = total_change / (len(values) - 1)


# Find max value and month is occurred
maxvalue = max(values)
max_index = values.index(maxvalue)

# Find min value and month it occurred
minvalue = min(values)
min_index = values.index(minvalue)

# Print results to terminal

print(f"Total Months: {rowcount}")
print(f"Total: {netprofit}")
print(f"Average Change: {round(average_change, 2)}")
print(f"Greatest Profit Increase: {months[max_index]} ({str(maxvalue)})")
print(f"Greatest Profit Decrease: {months[min_index]} ({str(minvalue)})")

# Print results to text file

with open('analysis/bankresults.txt', 'w') as f:
    l1 = f"Total Months: {rowcount} \n"
    l2 = f"Total: {netprofit} \n"
    l3 = f"Average Change: {round(average_change, 2)} \n"
    l4 = f"Greatest Profit Increase: {months[max_index]} ({str(maxvalue)}) \n"
    l5 = f"Greatest Profit Decrease: {months[min_index]} ({str(minvalue)})"
    f.writelines([l1, l2, l3, l4, l5])