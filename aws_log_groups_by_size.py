# pip install nose --user
# pip install tornado --user
# pip install boto3 --user
# pip install prettytable --user


import boto3
import json
from hurry.filesize import alternative
from prettytable import PrettyTable

# get log groups
client = boto3.client('logs')
log_groups = [] #client.describe_log_groups()

# create logs list
logs = []

paginator = client.get_paginator('describe_log_groups')
iterator = paginator.paginate(PaginationConfig={'MaxItems': 10000})
for page in iterator:
  for log_group in page['logGroups']:
    # add logs to list
    if log_group['storedBytes'] > 1000000: # 1mb
      logs.append({
        'log_group_name': log_group['logGroupName'],
        'retention_in_days': log_group.get('retentionInDays', 'Never Expire'),
        'stored_bytes': log_group['storedBytes']
      })

# sorting function
def sortBySize(e):
  return e['stored_bytes']

# human readable size function
suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
def humansize(nbytes):
  i = 0
  while nbytes >= 1024 and i < len(suffixes)-1:
    nbytes /= 1024.
    i += 1
  f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
  return '%s %s' % (f, suffixes[i])

# sort logs
logs.sort(reverse=True, key=sortBySize)

# add table headers
t = PrettyTable(['log_group_name', 'retention_in_days', 'stored_bytes'])
t.align['log_group_name'] = 'l'
t.align['stored_bytes'] = 'r'

# populate table
for x in logs:
  t.add_row([x['log_group_name'], x['retention_in_days'], humansize(x['stored_bytes'])])

# print pretty table
print(t)