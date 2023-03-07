import csv
import time

active_users_list = []
adobe_users_list = []
free_licenses = []


def main():
    print("\nThis tool will help you audit Adobe licenses.")
    print("If you have not yet, please download the lists of adobe users by groups.")
    print("\nSimilarly, if you have not yet, please download the list of active users from HR.")
    print("You will have to export this list from xlsx to csv. Do not edit the tables.")
    input("\nAre you ready to start? Press any key to continue")
    
    get_active_users()
    get_adobe_users()
    crosscheck_users(adobe_users_list, active_users_list)
    
    print("\n\nThese are the users who are not on the list of active employees, but still have Adobe licenses:")
    print(free_licenses)
    print("\nIt appears there are %s licenses to be freed." % len(free_licenses))
    print("\n*Please double check these users before removing their licenses*\n")
    
    
def get_active_users():
    filepath = input("\nclick and drag the active users csv file here: ").strip("'")
    if filepath == "" or filepath == " ":
        print("Empty filepath detected, try again")
        get_active_users()
        return

    try:
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                active_users_list.append(row[1].lower())       
    except Exception as e:
        print("An error occurred while reading the file")
        print(e)
        get_active_users()
        return   


def get_adobe_users():
    filepath = input("\nclick and drag adobe users csv file here: ").strip("'")
    if filepath == "" or filepath == " ":
        print("Empty filepath detected, skipping...")
        get_adobe_users()
        return 
    
    try:
        with open(filepath, 'r') as f:
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                adobe_users_list.append(row[1].lower())
    except Exception as e:
        print("An error occurred while reading the file")
        print(e)
        get_adobe_users()
        return

        
    morefiles = input("Are there more adobe users files? enter 'y' or 'n': ")
    if morefiles == "y":
        get_adobe_users()
    elif morefiles == "" or morefiles == " ":
        print("This is not a valid filepath, try again.\n")
        get_adobe_users()
        return
        
    
def crosscheck_users(adobe_users_list, active_users_list):
    print("Starting checks...")
    time.sleep(1)
    adobeusers_set = set(adobe_users_list)
    for adobeuser in adobeusers_set:
        if adobeuser == "username":
            continue
        elif adobeuser not in active_users_list:
            free_licenses.append(adobeuser)
        
       
if __name__ == "__main__":
    main()