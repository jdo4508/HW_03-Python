# Import OS & CSV Modules
import os
import csv
import sys

# # Create list for each column
month = []
profit = []
monthly_change =[]
profit_change = []

# Create path from the Resources folder
filepath = os.path.join ('..', 'Resources', 'budget_data.csv')

# Read in CSV File with Delimiter commas
with open(filepath, 'r') as csvfile:
    csvreader = csv.reader (csvfile, delimiter = ',')
    #print(csvreader)

# Define first row as header
    csv_header = next(csvreader)
    #print(f"Header: {csv_header}")

# Calculate total months
    for row in csvreader:
        month.append(row[0])
        profit.append(row[1])
    #print(len(month))

 # Calcuate total profit
    profit_int = map(int,profit)
    total_profit = (sum(profit_int))
    #print(total_profit)

# Calculate average revenue
    x = 0
    for x in range(len(profit) - 1):
        change = int(profit[x+1]) - int(profit[x])
        profit_change.append(change)
        total = sum (profit_change)
        #print(profit_change)

        monthly_change = total / len(profit_change)
        #print(monthly_change)

# Calculate maximun profit increase
    profit_increase = max(profit_change)
    #print(profit_increase)
    y = profit_change.index(profit_increase)
    month_increase = month[y+1]

# Calculate maximim profit decrease
    profit_decrease = min(profit_change)
   # print(profit_decrease)
    z = profit_change.index(profit_decrease)
    month_decrease = month[z+1]

# Print final parameters
    print("Total Months:" + str(len(month)))
    print("Total Profits: $" + str(total_profit))
    print("Average Profit Change: $ "+ str(monthly_change)) #ugggggh i cant figure out how to make this 2 decimal places!!
    print(f"Greatest Profit Increase: {month_increase} (${profit_increase})")
    print(f"Greatest Profit Decrease: {month_decrease} (${profit_decrease})")

#Create output .txt file
##blarrgggghhhhh i looked this up and it works but not how we did it in class!

sys.stdout = open("profit_results.txt", "w")
print("Total Months:" + str(len(month)))
print("Total Profits: $" + str(total_profit))
print("Average Profit Change: $ "+ str(monthly_change)) 
print(f"Greatest Profit Increase: {month_increase} (${profit_increase})")
print(f"Greatest Profit Decrease: {month_decrease} (${profit_decrease})")
sys.stdout.close()