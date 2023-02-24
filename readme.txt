Hello!

This tool will help you audit the Adobe licenses. 

Quickstart:

1. Download csv files of all adobe users from SoFi and put those files into the csv folder you see here.
2. export the xlsx file of all active employees to csv, then put it into the csv folder you see here.
3. Rename the csv file containing all SoFi employees so that it no longer has spaces. This is good practice in general.
3. open a terminal window, navigate to this folder, and run "python3 adobeaudit.py".
4. double check users that are returned before removing their licenses. 


Longstart:

If you have not yet, please download the lists of adobe users by groups.
These will download with the name of user1, user2, etc. Please do not change the names.
Similarly, if you have not yet, please download the lists of active users from HR.
You will have to export this list from xlsx to csv. You can name it something like 'active_employees.csv' or similar.
The name must contain the words active employee somehow, and it must be a csv file.
Place this into the csv directory too.

