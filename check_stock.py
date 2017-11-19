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

def send_email(msg_content, from_address, to_address):
    formatted_message = '\n'.join(msg_content)
    message = MIMEText(formatted_message, 'html')

    message['From'] = from_address
    message['To'] = to_address
    message['Subject'] = 'Lenovo laptops in stock'

    msg_full = message.as_string()

    recipients = 'aldonmez@gmail.com'

    server = smtplib.SMTP('smtp-relay.gmail.com:587')
    server.starttls()
    server.login('adonmez@homefinder.com', 'qweasdzxciukjmn12!!')
    try:
        server.sendmail('adonmez@homefinder.com', recipients,
                        msg_full)
        server.quit()
    except Exception as e:
        print "ERROR: " + str(e)

if __name__ == "__main__":
    list_of_in_stock_laptops = []
    os.chdir('lenovo_outlet/lenovo_outlet')
    # output_json_to_directory('../../test.json')
    # sleep(5)
    with open('/home/al/code/projects/lenovo_outlet_stock/test.json') as f:
        try:
            json_objects = json.load(f)
        except Exception as e:
            print "Error" + e
            raise
        for laptop in json_objects:
            if check_laptop_matches_request('ThinkPad', laptop):
                if check_laptop_in_stock(laptop):
                    list_of_in_stock_laptops.append(laptop['name'])
    if list_of_in_stock_laptops > 0:
        send_email(list_of_in_stock_laptops, 'adonmez@homefinder.com', 'aldonmez@gmail.com')
        print(type(list_of_in_stock_laptops))