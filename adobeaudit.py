import csv
import time

active_users = []
adobe_users = []
free_licenses = []

def main():
    print("This tool will help you audit Adobe licenses.")
    print("If you have not yet, please download the lists of adobe users by groups.")
    print("\nSimilarly, if you have not yet, please download the lists of active users from HR.")
    print("You will have to export this list from xlsx to csv. Do not edit the tables.")
    input("Are you ready to start? Press enter to continue...or ^c to exit...")
    
    
    get_active_users()
    get_adobe_users()
    crosscheck_users(adobe_users, active_users)
    print("\n\nThese are the users who are not on the list of active employees, but still have Adobe licenses:")
    print(free_licenses)
    print("\nThere are %s licenses free." % len(free_licenses))
    print("\n*Please double check these users before removing their licenses*\n")
    
    
def get_active_users():
    filepath = input("click and drag the active_users csv file here: ").strip("'")
    
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        
        for row in reader:
            active_users.append(row[1].lower())       
    

def get_adobe_users():
    filepath = input("click and drag adobe users csv file here: ").strip("'")
    
    with open(filepath, 'r') as f:
        reader = csv.reader(f, delimiter=",")
            
        for col in reader:
            adobe_users.append(col[1].lower())
            
    morefiles = input("Are there more adobe users files? enter 'y' or 'n': ")
    if morefiles == "y":
        get_adobe_users()
    else:
        print("Starting checks...")
        time.sleep(1)
   
        
def crosscheck_users(adobe_users, active_users):
    ad_users = set(adobe_users)
    for adobeuser in ad_users:
        if adobeuser == "username":
            continue
        elif adobeuser not in active_users:
            free_licenses.append(adobeuser)
        
       
if __name__ == "__main__":
    main()