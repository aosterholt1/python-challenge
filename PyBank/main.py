import os 
import csv

csvpath = os.path.join("/Users/aosmacbookpro/Desktop/gitlab-data-analytics/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv")
no_months= []
total_netprofit = []
profitchange = []


with open(csvpath, newline= '') as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ',')
	header = next(csvfile)
	
	for row in csvreader:
		no_months.append(row[0])
		total_netprofit.append(int(row[1]))
	
	for i in range(len(total_netprofit)-1):
	
		profitchange.append(total_netprofit[i+1]-total_netprofit[i])
	
max_value = max(profitchange)
min_value = min(profitchange)

max_valuemonth = profitchange.index(max(profitchange))+1
min_valuemonth = profitchange.index(min(profitchange))+1
		
		
print (f"Total months: {len(no_months)}")
print(f"Total :${sum(total_netprofit)}")
print(f"Average Change: {round(sum(profitchange)/len(profitchange),2)}")
print(f"Greatest Increase in profits: {no_months[max_valuemonth]} (${(str(max_value))})")
print(f"Greatest Decrease in profits: {no_months[min_valuemonth]} (${(str(min_value))})")

# save the output file path
output_file = os.path.join("Python Summary.txt")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as file:
    #writer = csv.writer(datafile)

    file.write("Homework 3 Python")
    file.write("\n")
    file.write("Financial Analysis")
    file.write("\n")    
    file.write("---------------------")
    file.write("\n")
    file.write(f"Total months: {len(no_months)}")
    file.write("\n")
    file.write(f"Total :${sum(total_netprofit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(profitchange)/len(profitchange),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in profits: {no_months[max_valuemonth]} (${(str(max_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in profits: {no_months[min_valuemonth]} (${(str(min_value))})")

    #writer.writerows(output_file)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    