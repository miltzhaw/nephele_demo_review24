#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wotpy.functions.functions import vo_status, device_status

# async def triggerBringup_handler(params):
#     # How to get the launch file ID param to trigger the bringup?
#     launchfileID = await consumed_vos["tb2"].properties['possibleLaunchfiles'].read()
#     result = {"launchfile to bring up": launchfileID}
#     print(result)
#     return result

#### Not sure if we need it ####
# async def check():
#     curr_vo_status = await vo_status(exposed_thing, 1)
#     curr_device_status = await device_status(exposed_thing, "http://160.85.253.140:9090", 1)

#     print(f"Status VO: {curr_vo_status}")
#     print(f"Status Device: {curr_device_status}")

async def read_property_from_tb2():
    # Initialize the property values
    allAvailableResources = await consumed_vos["tb2"].properties['allAvailableResources'].read(
        # {
        #'battery_percent': read_from_sensor('kobuki: Battery')[0],
        #'battery_charging': read_from_sensor('kobuki: Battery')[1],
        #}
    )
    possibleLaunchfiles = await consumed_vos["tb2"].properties['possibleLaunchfiles'].read()
    # Initialize the property values
    await exposed_thing.properties['allAvailableResources'].write(allAvailableResources)
    await exposed_thing.properties['possibleLaunchfiles'].write(possibleLaunchfiles)
