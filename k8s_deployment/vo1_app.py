#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wotpy.functions.functions import vo_status, device_status

async def read_property_from_tb2():
    # Initialize the property values
    allAvailableResources = await consumed_vos["tb2"].properties['allAvailableResources'].read(
    )
    possibleLaunchfiles = await consumed_vos["tb2"].properties['possibleLaunchfiles'].read()
    
    # Initialize the property values
    await exposed_thing.properties['allAvailableResources'].write(allAvailableResources)
    await exposed_thing.properties['possibleLaunchfiles'].write(possibleLaunchfiles)


