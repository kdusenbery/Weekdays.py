"""
Kohl Dusenbery
ENTD200
Prof. Edeki
Week 8
Aug 27, 2017
"""

weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
counter = 0
input_data = 'yes' 
while input_data == 'yes':
    print (weekDays[counter])
    counter+=1      
    if counter < len(weekDays) and counter != 0:
        input_data = input("Do you want to proceed?(yes/no)")
    else:
        counter = 0
        input_data = input("Do you want to proceed?(yes/no)")
