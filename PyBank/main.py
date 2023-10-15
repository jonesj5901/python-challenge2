import os
import csv

from numpy import mean

budgetCsv = os.path.join("PyBank", "Resources", "budget_data.csv")

with open(budgetCsv) as csvFile:
    # get the wrapper and store it as a reader using the .reader() function
    csvReader = csv.reader(csvFile, delimiter=",")

    csvHeader = next(csvReader)

    # variables and conditions
    profNloss = []
    date = []
    totalAmt = 0

    for row in csvReader:
        profNloss.append(int(row[1]))
        date.append(row[0])
        
        totalMonths = len(date)
    # The total number of months included in the dataset
        totalAmt += int(row[1])
    # The net total amount of "Profit/Losses" over the entire period
        profChange = []
    for col in range(1, len(profNloss)):
        # The changes in "Profit/Losses" over the entire period, and then the average of those changes
        profChange.append((int(profNloss[col]) - int(profNloss[col - 1])))
        avgChange = round(sum(profChange) / len(profChange),2)

        greatestInc = max(profChange)
        greatestDec = min(profChange)

grtDecdate = date[profChange.index(min(profChange))+1]
grtIncdate = date[profChange.index(max(profChange))+1]

with open("PyBank.txt", "wt") as f:
    print("Financial Analysis", file = f)
    print(".........................................................................", file = f)
    print(f"Total Months: {totalMonths}", file = f)
    print(f"Total: ${totalAmt}", file = f)
    print(f"Average Change: ${avgChange}", file = f)
    print(f"Greatest Increase in Profits: {grtIncdate} (${greatestInc})", file = f)
    print(f"Greatest Decrease in Profits: {grtDecdate} (${greatestDec})", file = f)