#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio

import requests
from flask import Flask, render_template, request

from wotpy.wot.servient import Servient
from wotpy.wot.wot import WoT
from wotpy.protocols.http.client import HTTPClient

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trigger_execution', methods=['POST'])
def trigger_execution():
    result = asyncio.run(trigger())
    print("trigger", result)
    return render_template('index.html', execution_status=result)

async def trigger():
    http_client = HTTPClient()
    security_scheme_dict = {
        "scheme": "bearer"
    }
    credentials_dict = {
        "token": "token"
    }
    http_client.set_security(security_scheme_dict, credentials_dict)
    wot = WoT(servient=Servient(clients=[http_client]))
    consumed_thing = await wot.consume_from_url("http://vo1:9090/vo1")
   #desired_launch_file_id = "startmapping"
    result = await consumed_thing.invoke_action("triggerBringup", {'launchfileId': "startmapping" }) # desired_launch_file_id=[bringup, startmapping, saveMap]
    return result

@app.route("/read_data")
def read_data():
    result = asyncio.run(read())
    print("read", result)
    return render_template('index.html', data=result)

async def read():
    http_client = HTTPClient()
    security_scheme_dict = {
        "scheme": "bearer"
    }
    credentials_dict = {
        "token": "token"
    }
    http_client.set_security(security_scheme_dict, credentials_dict)
    wot = WoT(servient=Servient(clients=[http_client]))
    consumed_thing = await wot.consume_from_url("http://vo1:9090/vo1")
    result = await consumed_thing.properties["allAvailableResources"].read()
    #result = await consumed_thing.invoke_action("currentValues")
    print(result)
    return result

if __name__ == "__main__":
    app.run(debug=True)

