#To DO Homework
# Import
import os
import csv

# Variables
total_months = 0
net_total_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

#Set Path for File


#Open and Read CSV File


    #CSV Reader Specifies Delimniter & Variable that Holds Contents
    csvreader = csv.reader(csvfile, delimiter=",")

    #Read Header Row First
    csv_header = next(csvreader)
    row = next(csvreader)

    #Calculate Total Number of Months, Net Amount of P&L, and Set Variables for Rows
    previous_row = int(row[1])
    total_months += 1
    net_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]

#Read Each Row of Data After the Header
for row in csvreader:
    #Calculate Total Number of Months Included in Dataset
    total_months += 1
    #Calculate Net Amount of P&L over Entire Period
    net_amount += int(row[1])

    #Calculate Change from CUrrent Month to Previous Month






    #Calculate the Greatest Increase





    #Calculate the Greatest Decrease




    #Calculate the Average & The Date
    average_change = sum(monthly_change)/ len(monthly_change)

    highest = max(monthly_change)
    lowest = min(monthly_change)

    #Now What???