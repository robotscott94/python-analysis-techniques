# read csv file
import os
import csv

bankData = os.path.join("Resources", "budget_data.csv")

#calculate total months in dataset
with open(bankData) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader, None)
    
    rowcount = 0
    for row in csvreader:
        rowcount += 1

    print("Total Months: " + str(rowcount))


# Calculate net profits/losses
with open(bankData) as csvfile:
    csvreader2 = csv.reader(csvfile, delimiter=',')

    next(csvreader2, None)

    netprofit = 0
    for row in csvreader2:
        netprofit += int(row[1])
    
    print("Total: " + str(netprofit))


# Calculate average changes
with open(bankData) as csvfile:
    csvreader3 = csv.reader(csvfile, delimiter=',')

    next(csvreader3, None)

    values = [float(row[1]) for row in csvreader3]

    total_change = 0
    for i in range(1, len(values)):
        total_change += values[i] - values[i - 1]
        
    average_change = total_change / (len(values) - 1)
    print("Average Change: " + str(round(average_change, 2)))


# Find date and amount of greatest profit increase
with open(bankData) as csvfile:
    csvreader4 = csv.reader(csvfile, delimiter=',')

    next(csvreader4, None)

    values = [float(row[1]) for row in csvreader4]

    maxvalue = max(values)
    max_index = values.index(maxvalue)
    

with open(bankData) as csvfile:   
    csvreader5 = csv.reader(csvfile, delimiter=',')

    next(csvreader5, None)

    months = [row[0] for row in csvreader5]

    print("Greatest Profit Increase: " +  months[max_index] + "  (" +  str(maxvalue) + ")")


# Find date and amount of greatest profit decrease
with open(bankData) as csvfile:
    csvreader6 = csv.reader(csvfile, delimiter=',')

    next(csvreader6, None)

    values = [float(row[1]) for row in csvreader6]

    minvalue = min(values)
    min_index = values.index(minvalue)

    print("Greatest Profit Decrease: " +  months[min_index] + "  (" +  str(minvalue) + ")")
    
    
    
