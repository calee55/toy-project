from hotdeal_parser import *
import schedule
import time

schedule.every(30).minutes.do(aggregate_hotdeal)

print("hotdeal aggregation start!")

while True:
    schedule.run_pending()
    time.sleep(1)
