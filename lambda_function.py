import requests
import json
import os

slackurl = os.environ['slackNotification']

def lambda_handler(event, context):
    
    print(event)
    
    try:
        hookdata = json.loads(event['body'])
    except:
        print("not json")
    
    if ( hookdata['action'] == "opened" ):
        prNumber = str(hookdata['number'])
        diffUrl = hookdata['pull_request']['html_url']
        data = "New pull request" + prNumber + " opened. Check the diff at " + diffUrl
        headers = {'Content-type': 'application/json'}
        response = requests.post(slackurl, json={"text":data}, headers=headers)
        print(response)
    elif ( hookdata['action'] == "reopened"):
        prNumber = str(hookdata['number'])
        diffUrl = hookdata['pull_request']['html_url']
        data = "Pull request " + prNumber + " reopened. Check the diff at " + diffUrl
        headers = {'Content-type': 'application/json'}
        response = requests.post(slackurl, json={"text":data}, headers=headers)
        print(response)
    elif ( hookdata['action'] == "closed"):
        prNumber = str(hookdata['number'])
        data = "Pull request " + prNumber + " closed."
        headers = {'Content-type': 'application/json'}
        response = requests.post(slackurl, json={"text":data}, headers=headers)
        print(response)
    elif ( hookdata['action'] == "merged"):
        prNumber = str(hookdata['number'])
        data = "Pull request " + prNumber + " merged."
        headers = {'Content-type': 'application/json'}
        response = requests.post(slackurl, json={"text":data}, headers=headers)
        print(response)
    else:
        print(hookdata)
