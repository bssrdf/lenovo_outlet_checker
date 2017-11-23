The scraper is fully functional

### Usage    
1. Pip install requirements    
2. Modify 'laptops_to_search' on line 45 is necessary. It's currently set to: 'Thinkpad x1', 'Thinkpad 460', 'Thinkpad 470'. 
3. Enter SMTP relay information in 'send_email' function in 'check_stock.py' - line 65    
4. Run 'check_stock.py' to run crawler and send email if a ThinkPad is in stock.   