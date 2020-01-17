import json
import re

def serch_maintenance(notice):
    #print(notice['notifications'])
    report = []
    for line in notice['notifications']:
        if line['type'] == 'Maintenance':
            if re.search('VPS', line['contents']):
                report.append({'title':line['title'], 'contents':line['contents']})
    return report
