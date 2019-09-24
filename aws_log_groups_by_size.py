# pip install nose --user
# pip install tornado --user
# pip install boto3 --user
# pip install hurry.filesize --user
# pip install prettytable --user


import boto3
import json
from hurry.filesize import size
from prettytable import PrettyTable

# get log groups
logs = boto3.client('logs')
log_groups = logs.describe_log_groups()

# create logs list
logs = []

# add logs to list
for log_group in log_groups['logGroups']:
  if log_group['storedBytes'] > 1000000: # 1mb
    logs.append({
      'log_group_name': log_group['logGroupName'],
      'retention_in_days': log_group.get('retentionInDays',
      'Never Expire'), 'stored_bytes': log_group['storedBytes']
    })

# sorting function
def sortBySize(e):
  return e['stored_bytes']

# sort logs
logs.sort(reverse=True, key=sortBySize)

# add table headers
t = PrettyTable(['log_group_name', 'retention_in_days', 'stored_bytes'])

# populate table
for x in logs:
  t.add_row([x['log_group_name'], x['retention_in_days'], size(x['stored_bytes'])])

# print pretty table
print(t)