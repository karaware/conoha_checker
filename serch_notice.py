import json
import re
from datetime import datetime

def serch_maintenance(notice):
    report = []
    for line in notice['notifications']:
        linedate = re.sub('T.+Z', '', line['start_date'])
        #if datetime.strptime(linedate, '%Y-%m-%d') == datetime.today():
        #if datetime.strptime(linedate, '%Y-%m-%d') == datetime.strptime('2019-10-11', '%Y-%m-%d'):
        if line['type'] == 'Maintenance':
            if line['type'] == 'Maintenance':
                if re.search('VPS', line['contents']):
                    report.append({'title':line['title'], 'contents':line['contents']})
    return report
