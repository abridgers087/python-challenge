#Module 3 Challenge
#Analyze budget_data.csv. Dataset contains two columns: Date (day-month) and Profit/Losses (large numbers)

#import modules
import os
import csv

#set incoming file path
budget_data_csv = os.path.join(".", 'Resources', "budget_data.csv")

#set outgoing file path
budget_output = os.path.join(".", 'analysis', "budget_results.txt")

#setup variables
total_months = []
total_profits = 0 
previous_data = 0
pl_change_list = []
pl_change_average = 0
pl_change = 0
month = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999999999999999999]

#open and read the csv file
with open(budget_data_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    #skip the header
    csv_header = next(csv_reader)

    #loop through the rows to add months 
    for row in csv_reader:
        
        #find total months
        total_months.append(row[0])
        
        #find total profits/losses
        total_profits = total_profits + int(row[1])

        #find change in P&L
        pl_change = int(row[1]) - previous_data
        previous_data = int(row[1])
        pl_change_list = pl_change_list + [pl_change]
        month = month + [row[0]]

        #find the greatest increase
        if (pl_change > greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = pl_change

        #find the greatest decrease
        if(pl_change < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = pl_change        
        
    #print(len(total_months)) = 86. this is right. set to a variable for your final output
    final_total_months = len(total_months)
    
#find the average
pl_change_average = sum(pl_change_list) / final_total_months
#print(pl_change_average)

#print to Terminal, use a var to call easier for text output
output = (
    f"\nFinancial Analysis\n"
    f"-------------------------------------------\n"
    f"Total Months: {final_total_months}\n"
    f"Total Profts: ${total_profits}\n"
    f"Average Revenue Change: ${pl_change_average}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} ${greatest_increase[1]}\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} ${greatest_decrease[1]}\n"
        )

#print output to terminal
print(output)

#export and print to text file
with open(budget_output, "w") as txt_file:
    txt_file.write(output) 


    
