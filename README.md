The scraper works, and it crawls all pages listing Thinkpads. Sending of email works with proper SMTP relay and creds.    

###Usage    
Pip install requirements    
Enter SMTP relay information in 'send_email' function in 'check_stock.py'.    
Run 'check_stock.py' to run crawler and send email if a ThinkPad is in stock.     
Modify array 'laptops_to_search' in check_stock to add or remove laptops to search. It's currently set to'Thinkpad x1', 'Thinkpad 460', 'Thinkpad 470'.    