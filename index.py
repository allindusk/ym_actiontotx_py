import time
import os
import json
from datetime import datetime
from dateutil import tz

def runscript(scriptstr):
  for scriptname in scriptstr.split('&&'):
    print(datetime.now(tz=tz.gettz('Asia/Shanghai')),'执行'+scriptname)
    os.system('python3 ./'+scriptname+'.py')
    print(datetime.now(tz=tz.gettz('Asia/Shanghai')),'执行结束'+scriptname)

def main_handler(event, context):
  if 'Message' in event:
    #nocron|1.py&&2.py
    eventm = event['Message'].split('|')
    runtype = eventm[0]
    scriptstr=''
    if 'cron'== runtype:
      config = __import__("config")
      scriptstr = config.getscriptstr()
      runscript(scriptstr)
    elif 'nocron'== runtype:
      runscript(eventm[1])
  
  return json.dumps(event, indent = 2)