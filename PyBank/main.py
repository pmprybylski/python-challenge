#Dependencies
import os
import csv

#Files
data_file = 'Resources/budget_data.csv'
analysis_file = 'analysis/financial_analysis.txt'

#Variables to track
total_months = 0
total_revenue = 0

prev_revenue = 0
revenue_change = 0
greatest_increase = ['', 0]
greatest_decrease = ['', 99999999999999999]

revenue_changes = []

#Read Files
with open(data_file, 'r') as revenue_data:
    csvreader = csv.DictReader(revenue_data, delimiter=',')
    print(csvreader)
    
    #Bypass header
    csvheader = next(csvreader)
    print(csvheader)

    #Loop through rows
    for row in csvreader:

        #Calculate totals
        total_months = total_months + 1
        total_revenue = total_revenue + int(row['Profit/Losses']) #getting error, check in class to resolve
        #print(row)

        #Track changes
        revenue_change = int(row['Profit/Losses']) - prev_revenue
        #print(revenue_change)

        #Reset value of prev_revenue
        prev_revenue = int(row['Profit/Losses'])
        # print(prev_revenue)

        #Determine greatest increase
        if (revenue_change > greatest_increase[1]):
            greatest_increase[1] = revenue_change
            greatest_increase[0] = row['Date']

        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = row['Date']

        #Add to revenue_changes list
        revenue_changes.append(int(row['Profit/Losses']))
    
    #Set the revenue average
    revenue_avg = sum(revenue_changes) / len(revenue_changes)

    #Output display
    print()
    print()
    print()
    print('Finanacial Analysis')
    print('-------------------------------')
    print('Total Months: ' + str(total_months))
    print('Total Revenue: ' + str(total_revenue))
    print('Average Change: ' + str(sum(revenue_changes) / len(revenue_changes)))
    print('Greatest Increase: ' + str(greatest_increase[0]) + ' ($' +  str(greatest_increase[1]) + ')') 
    print('Greatest Decrease: ' + str(greatest_decrease[0]) + ' ($' +  str(greatest_decrease[1]) + ')')

#Output file
with open(analysis_file, "w") as txt_file:
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total Revenue: " + "$" + str(total_revenue))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")






