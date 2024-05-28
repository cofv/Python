import datetime

import math

date_1_input = input("Put in time where you want to start to count elec price ").split(" ")
date_2_input = input("and where do you want to end the time? ").split(" ")
ström_kwh = int(input("Hur mycket ström använder du i kwh per dag? "))
kostnad_kwh = int(input("Hur mycket kostar strämmen i öre/kwh "))

st = datetime.datetime(int(date_1_input[0]), int(date_1_input[1]),int(date_1_input[2]))
sl = datetime.datetime(int(date_2_input[0]), int(date_2_input[1]),int(date_2_input[2]))

date_diff = (sl - st).days

kostnad = date_diff * ström_kwh * kostnad_kwh

print(kostnad / 100, "kr")

"""
start_datum
slut_datum
hur mycket ström man använt i kwh
hur mycket strömmen kostan i öre/kwh
daglig kostnad ex 2kr
.now

"""