"""
=============================
ᕕ(◠ڼ◠)ᕗ
@time:2024/4/20 20:10
@IDE:PyCharm
=============================
"""

from datetime import datetime
from playsound import playsound
import time as systime

time = input('请输入闹钟想起时间：（如HH:MM;SS)\n')
hour, minute, second = map(int,time.split(':'))
print('闹钟已建立')

while True:
    now = datetime.now()
    if now.hour == hour and now.minute == minute and now.second == second:
        print('闹钟响了')
        playsound('Fantaisie_Impromptu_Op_66.mp3')
        break
    systime.sleep(1)