# Modules
import os
import csv
# import pandas as pd

# Set path for file
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# filename = input("Enter the filename:  ")
# os.chdir(os.path.dirname("c:/test/"))
# filepath = os.path.join("c:/test/", filename)

# print(filepath)
# Bonus
# ------------------------------------------
# Set variable to check if we found the video
found = False
print("\n----------------------\n")
# Open the CSV
file = open("c:/test/test.txt")
# file = open(filepath)

mystr = file.read()
newstr = mystr

newstr = newstr.replace("\n\n","===")
newstr = newstr.replace("\n, \n2021","-2021")
newstr = newstr.replace("\n, ","")
newstr = newstr.replace("\n","**")


# newstr = newstr.replace("**  **", ",")
newstr = newstr.replace("** - **", " - ")
newstr = newstr.replace("pm ","pm")
newstr = newstr.replace(" **","-")
newstr = newstr.replace("**Details**", "\n")
newstr = newstr.replace("**Search**", "\n")
newstr = newstr.replace("**", ",")
newstr = newstr.replace(",Career", "Career")
newstr = newstr.replace(", ", "; ")


newstr = newstr.replace("Past Career Services Online Events", "")
newstr = newstr.replace("Events previously offered by Career Services", "")
newstr = newstr.replace("Powered by Trilogy Education Services; a 2U; Inc. brand.", "")
newstr = newstr.replace("Privacy","")
newstr = newstr.replace("Terms of Use","")
newstr = newstr.replace("Cookie Policy","")
newstr = newstr.replace("CONTACT THE ORGANIZER","")
newstr = newstr.replace("You are a... Student Alum Industry Professional","")
newstr = newstr.replace("Job Seeking Yes No","")
newstr = newstr.replace("Employed Yes No","")

print(newstr)

# line = file.read().replace("\n", " ")
file.close()

file = open("c:/test/events.txt", 'w')
file.write(newstr)
file.close()


file1 = open("c:/test/events.txt")
In_text = csv.reader(file1, delimiter = ',')
 
file2 =open("c:/test/Events.csv",'w')
out_csv = csv.writer(file2)
 
file3 = out_csv.writerows(In_text)
 
file1.close()
file2.close()



# dframe = pd.read_csv("c:/test/newfile.txt") 

# # storing this dataframe in a csv file 
# dframe.to_csv('Online Events.csv',  index = None) 


print("\n----------------------\n")