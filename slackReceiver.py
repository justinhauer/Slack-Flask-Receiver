from slackclient import SlackClient
from flask import json, Flask, request
import json, requests, os

app = Flask(__name__)

@app.route('/postjson', methods = ['POST'])
def postJsonHandler():
    content = request.get_json()
    caller = str(content["caller"])
    time = str(content["eventTimestamp"])
    eventType = str(content["operationName"])
    slack_token = "your-slack-token-here"
    sc = SlackClient(slack_token)
    parsedJson = {"name of invoker":caller, "time of event": time, "type of event": eventType}
    outputObject = str(parsedJson)
    sc.api_call(
      "chat.postMessage",
      channel="Channel-ID",
      text = outputObject)
    return str(outputObject)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 5010)
