I plan on purchasing a ThinkPad soon, and I'd like to do it from Lenovo Outlet's site, so I'm working on this project. It is not yet complete.    

The scraper works, but needs the following:    
1. Change spider class from 'Spider' to 'CrawlSpider', and then add logic to crawl 'next page'    
2. Format e-mail message better    

Sending of email works with proper SMTP relay and creds, but there are variables in the "send_email" function in 'check_stock.py' I have not added yet as parameters, and those must be filled in to work.    

Run 'check_stock.py' to run crawler and send email if a ThinkPad is in stock.    