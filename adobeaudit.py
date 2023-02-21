import csv
import os


active_users = []
adobe_users = []
free_licenses = []

def main():
    print("This tool will help you audit Adobe licenses.")
    print("If you have not yet, please download the lists of adobe users by groups.")
    print("These will download with the name of user1, user2, etc. Please do not change the names.")
    print("\n***YOU MUST PLACE THESE IN THE CSV DIRECTORY***")
    print("\nSimilarly, if you have not yet, please download the lists of active users from HR.")
    print("You will have to export this list from xlsx to csv. You can name it something like 'active_employees.csv' or similar.")
    print("The name must contain the words active employee somehow, and it must be a csv file.")
    print("Place this into the csv directory too.\n")
    input("Are you ready to start? Press enter to continue...or ^c to exit...")
    
    
    get_active_users()
    get_adobe_users()
    crosscheck_users(adobe_users, active_users)
    print("\n\nThese are the users who are no longer active, but still have Adobe licenses:")
    print(free_licenses)
    print("\nThere are %s licenses free." % len(free_licenses))
    print("\n*Please double check these users before removing their licenses*\n")
    

def get_active_users():
    for file in os.listdir('csv'):
        if 'active' in file or 'employees' in file and file.endswith('.csv'):
            with open('csv/active_employees.csv', 'r') as f:
                reader = csv.reader(f)
                
                for row in reader:
                    active_users.append(row[1].lower())       
    
        
def get_adobe_users():
    for file in os.listdir('csv'):
        if file.startswith('users') and file.endswith('.csv'):
            with open('csv/%s' % file, 'r') as f:
                reader = csv.reader(f, delimiter=",")
                    
                for col in reader:
                    adobe_users.append(col[1].lower())
            
           
def crosscheck_users(adobe_users, active_users):
    ad_users = set(adobe_users)
    for adobeuser in ad_users:
        if adobeuser == "username":
            continue
        elif adobeuser not in active_users:
            free_licenses.append(adobeuser)
        
       
if __name__ == "__main__":
    main()