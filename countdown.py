#
# Countdown
#

from datetime import datetime

target_datetime = datetime.strptime('2024-04-26 17:00:00', '%Y-%m-%d %H:%M:%S')

now = datetime.now()

delta = target_datetime - now

print(delta)
