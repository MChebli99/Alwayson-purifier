import os
from pyvesync import VeSync

email = os.environ['VESYNC_EMAIL']
password = os.environ['VESYNC_PASSWORD']

manager = VeSync(email, password, time_zone="Asia/Beirut")
manager.login()
manager.update()

for purifier in manager.fans:
    print(f"{purifier.device_name} status: {purifier.device_status}")
    if purifier.device_status != "on":
        purifier.turn_on()
        print(f"Turned ON {purifier.device_name}")