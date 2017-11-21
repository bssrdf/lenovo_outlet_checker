import os
from time import sleep
import json
from email.mime.text import MIMEText
import smtplib

# Overwrites JSON file each time it runs
def output_json_to_directory(path):
    os.system('scrapy crawl lenovo -t json -o - > ' + path)

def check_laptop_matches_request(laptop_name, json_object):
    if laptop_name.lower() in json_object['name'].lower():
        return True

def check_laptop_in_stock(json_object):
    if 'in stock'.lower() in json_object['stock'].lower():
        return True

def send_email(msg_content, from_address, to_address, 
    smtp_addr, smtp_user, smtp_password):
    formatted_message = '\n'.join(msg_content)
    message = MIMEText(formatted_message, 'html')

    message['From'] = from_address
    message['To'] = to_address
    message['Subject'] = 'Lenovo laptops in stock'

    msg_full = message.as_string()

    server = smtplib.SMTP(smtp_addr)
    server.starttls()
    server.login(smtp_user, smtp_password)
    try:
    # to_address can be multiple addresses separated by a comma. ex.
    # 'name@email.com, name2@email.com'
        server.sendmail(smtp_user, to_address,
                        msg_full)
        server.quit()
    except Exception as e:
        print 'ERROR: ' + str(e)

if __name__ == "__main__":
    laptops_to_search = ['Thinkpad x1', 'Thinkpad 460', 'Thinkpad 470']
    list_of_in_stock_laptops = []
    os.chdir('lenovo_outlet/lenovo_outlet')
    output_json_to_directory('../../laptops_scraped.json')
    sleep(5)
    with open('../../laptops_scraped.json') as f:
        try:
            json_objects = json.load(f)
        except Exception as e:
            print "ERROR: " + str(e)
            raise
        for laptop in json_objects:
            for laptop_type in laptops_to_search:
                if laptop_type.lower() in laptop['name'].lower():
                    if 'in stock' in laptop['stock'].lower():
                        list_of_in_stock_laptops.append(laptop['name'])
    if list_of_in_stock_laptops > 0:
        send_email(list_of_in_stock_laptops, )
        print(list_of_in_stock_laptops)