import asyncio
import os
from pyvesync import VeSync

async def main():
    email = os.environ['VESYNC_EMAIL']
    password = os.environ['VESYNC_PASSWORD']

    async with VeSync(email, password, time_zone="Asia/Beirut") as manager:
        await manager.login()
        if not manager.enabled:
            print("Login failed — check email/password secrets.")
            return

        await manager.update()

        for purifier in manager.devices.air_purifiers:
            print(f"{purifier.device_name} status: {purifier.state.device_status}")
            if purifier.state.device_status != "on":
                await purifier.turn_on()
                print(f"Turned ON {purifier.device_name}")

asyncio.run(main())