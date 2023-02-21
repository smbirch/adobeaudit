import csv

active_users = []
adobe_users = []
free_licenses = []

def get_active_users():
    with open('csv/active_employees.csv', 'r') as f:
        reader = csv.reader(f)
        
        for row in reader:
            active_users.append(row[1].lower())       
    
        
def get_adobe_users():
    with open('csv/users2wwq.csv', 'r') as f:
        reader = csv.reader(f, delimiter=",")
            
        for col in reader:
            adobe_users.append(col[1].lower())
      
           
def crosscheck_users(adobe_users, active_users):
   for adobeuser in adobe_users:
       if adobeuser == "username":
           continue
       elif adobeuser not in active_users:
        free_licenses.append(adobeuser)
        
       
get_active_users()
get_adobe_users()
crosscheck_users(adobe_users, active_users)
print(free_licenses)
print(len(free_licenses))