import csv

#Function to calculate the difference between the last and first profit
def get_last_minus_first(first_num, last_num):
    return last_num - first_num

# Open the CSV file containing budget data
with open('/Users/nguyengiang/Downloads/Starter_Code-4/PyBank/Resources/budget_data.csv', 'r') as csv_file:
    
    # Create a CSV reader object to read through the data
    budget_csv = csv.reader(csv_file)
    # Skip the header row (the first row that contains column names)
    next(budget_csv)
    
    # Read the first data row to initialize the variables
    first_row = next(budget_csv) # First row after the header
    first_num = int(first_row[1]) # The first profit/loss number
    num_months = 0
    total_profit = 0
    previous_profit = 0
    max_increase = 0
    max_increase_date = ""
    min_increase = 0
    min_increase_date = ""
    last_num = first_num
    total_change = 0

    # Loop through each row in the CSV file to calculate monthly data
    for row in budget_csv:
        num_months += 1 # Increment the number of months
        total_profit += int(row[1]) 
        last_num = int(row[1])
        date = row[0]
        current_profit = int(row[1])

        # Calculate the difference between the current profit and the previous month's profit  
        difference = current_profit - previous_profit
        total_change += difference # Add the difference to total change
        previous_profit = current_profit # Update the previous profit for the next iteration

        # Track the greatest increase in profits
        if difference > max_increase:
            max_increase = difference
            max_increase_date = date # Store the date of the greatest increase 
        # Track the greatest decrease in profits
        if difference < min_increase:
            min_increase = difference
            min_increase_date = date # Store te date of the greatest decrease
    
    # Calculate the average change in profits over the months
    total_change = get_last_minus_first(first_num, last_num)
    average_change = total_change / (num_months -1)

    # Print the results of the financial analysis
    print(f"Financial Analysis")
    print("-------------------------")
    print(f"Total Months: " + str(num_months))
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})")
    print(f"Greatest Decrease in Profits: {min_increase_date} (${min_increase})")
