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
    # return f"<p>{result}</p>"
    try:
        # Simulate execution by making an HTTP call
        response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
        if response.status_code == 200:
            execution_status = "Success"
        else:
            execution_status = "Failed"
    except Exception as e:
        execution_status = "Failed: " + str(e)
    
    return render_template('index.html', execution_status=execution_status)

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
    consumed_thing = await wot.consume_from_url("http://vo-tb2:9090/vo-tb2")
    result = await consumed_thing.invoke_action("triggerBringup", {'launchfileId': desired_launch_file_id }) # desired_launch_file_id=[bringup, startmapping, saveMap]
    print(result)
    return result

@app.route("/read_data")
def read_data():
    result = asyncio.run(read())
    print("read", result)
    # return f"<p>{result}</p>"
    try:
        # Simulate reading data by making an HTTP call
        response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
        data = response.json()
    except Exception as e:
        data = {"error": str(e)}
    
    return render_template('index.html', data=data)

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
    consumed_thing = await wot.consume_from_url("http://vo-tb2:9090/vo-tb2")
    result = await consumed_thing.properties["allAvailableResources"].read()
    return result

if __name__ == "__main__":
    app.run(debug=True)

