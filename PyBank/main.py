import csv

def get_last_minus_first(first_num, last_num):
    return last_num - first_num

with open('/Users/nguyengiang/Downloads/Starter_Code-4/PyBank/Resources/budget_data.csv', 'r') as csv_file:
    
    budget_csv = csv.reader(csv_file)
    next(budget_csv)
    
    first_num = int(first_row[1])
    num_months = 0
    total_profit = 0
    previous_profit = 0
    max_increase = 0
    max_increase_date = ""
    min_increase = 0
    min_increase_date = ""
    for row in budget_csv:
        num_months += 1
        total_profit += int(row[1])
        last_num = int(row[1])
        date = row[0]
        current_profit = int(row[1])
        if previous_profit !=0:
            difference = current_profit - previous_profit
        previous_profit = current_profit
        if difference > max_increase:
            max_increase = difference
            max_increase_date = date
        if difference < min_increase:
            min_increase = difference
            min_increase_date = date
   
    total_change = get_last_minus_first(first_num, last_num)
    average_change = total_change / (num_months -1)

    print(f"Financial Analysis")
    print("-------------------------")
    print(f"Total Months: " + str(num_months))
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})")
    print(f"Greatest Decrease in Profits: {min_increase_date} (${min_increase})")
