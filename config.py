import json
import os
import re
from datetime import datetime
from dateutil import tz

RUN_CONFIG=json.loads(os.environ['RUN_CONFIG'])if "RUN_CONFIG" in os.environ else ''

scriptobj_cron={
#==============常驻=================
  'xmly_speed':{#喜马拉雅极速版
    'url':'https://github.com/Zero-S1/xmly_speed/raw/master/xmly_speed.py',
    'cron':{'m':'23','h':'00,01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18,19,20,21,22,23'},
    'run':RUN_CONFIG['xmly_speed']['run'] if 'xmly_speed' in RUN_CONFIG else 'true'
  },
}
# scriptobj_nocron={
# #==============常驻=================
#   'nocron':{#nocron
#     'url':'https://github.com/nocron',
#   },
# }

scriptobj = {**scriptobj_cron}

def getallurl():
  urlarr=[]
  for script in scriptobj:
    urlarr.append(scriptobj[script]['url'])
  return urlarr

def getscriptstr():
  scriptstr=''
  nowtime =datetime.now(tz=tz.gettz('Asia/Shanghai'))
  hour = str(nowtime.hour)
  hour = '0'+hour if len(hour)<2 else hour
  minute = str(nowtime.minute)
  for key in scriptobj_cron:
    scriptobjvalue = scriptobj_cron[key]
    cron = scriptobjvalue['cron']
    if hour in cron['h'] and minute in cron['m'] and 'true' in scriptobjvalue['run']:
      scriptstr+=re.findall(r'\w+\.py', scriptobjvalue['url'], re.S)[0]+'&&'
  
  return scriptstr[0:len(scriptstr)-2]

