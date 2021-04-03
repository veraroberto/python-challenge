import os
import csv

resources_file = os.path.join("Resources","budget_data.csv")


#Initiate Variables
count_months = 0
total_profit = 0
sum_changes = 0
sum_dif = 0
greates_increase = 0
month_increase = ""
greates_decrease = 0 
month_decrease = ""

with open(resources_file) as csvfile:
   csv_reader = csv.reader(csvfile, delimiter=",")
   #HEADER
   csv_header = next(csvfile)

   row_count = 0

   for row in csv_reader:
       #Determine the First Value
       if row_count == 0:
           previous_month = float(row[1])
           row_count += 1

       
       total_profit = total_profit + float(row[1])
       count_months += 1
       sum_changes = sum_changes + float(row[1])
       

       #Calculate the Difference of Profit/loss and the Average
       dif = float(row[1]) - previous_month
       sum_dif = sum_dif + dif

       if dif >= greates_increase:
           greates_increase = dif
           month_increase = row[0]

       if dif <= greates_decrease:
           greates_decrease = dif
           month_decrease = row[0]
        
       previous_month = float(row[1])
       
       
average_changes = sum_dif /(count_months - 1)

print("Financial Analysis")
print("---------------------------------------------")
print(f'Total Months: {count_months}')

print(f'Total ${total_profit}')
print('Average Change: '+ "{:,.2f}".format(average_changes))

print('Greatest Increase in Profits: ' + str(month_increase) +" " + "{:,.0f}".format(greates_increase))
print('Greatest Decrease in Profits: '+ str(month_decrease) + " " + "{:,.0f}".format(greates_decrease))

#Write file
output_path = os.path.join("Analysis","Results.csv")


with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer     , delimiter=','
    csvwriter = csv.writer(csvfile)

    # Write the first row (column headers)
    csvwriter.writerow(['Financial Analysis'])

    csvwriter.writerow(['----------------------------'])
    #csvwriter.writerows([csv_header])
    csvwriter.writerow([f'Total Months: {count_months}'])
    csvwriter.writerow([f'Average Change: {average_changes}'])
    #csvwriter.writerow([f'Average Change: {:10.4f}'])
    csvwriter.writerow([f'Greatest Increase in Profits: {month_increase} {greates_increase}'])
    csvwriter.writerow([f'Greatest Decrease in Profits: {month_decrease} {greates_decrease}'])