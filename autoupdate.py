import time
from main import update_product,get_all_data,take_urls

while True:
    update_product(get_all_data(take_urls()))
    time.sleep(3600)