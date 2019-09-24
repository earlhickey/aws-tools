# AWS tools
Some management tools for AWS

# PIP

## Install pip

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && sudo python get-pip.py

## AWS credentials
The scripts are using local AWS credentials see:

https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration

# Scripts

## python aws_log_groups_by_size.py
Output a list of CloudWatch logs ordered by size
```
+----------------------------------------------+-------------------+--------------+
|                log_group_name                | retention_in_days | stored_bytes |
+----------------------------------------------+-------------------+--------------+
| /aws/appsync/apis/xxxxxxxxxxxxxxxxxxxxxxxxxx |    Never Expire   |     103M     |
| /aws/appsync/apis/xxxxxxxxxxxxxxxxxxxxxxxxxx |    Never Expire   |     11M      |
| /aws/appsync/apis/xxxxxxxxxxxxxxxxxxxxxxxxxx |         14        |      2M      |
| /aws/appsync/apis/xxxxxxxxxxxxxxxxxxxxxxxxxx |         7         |      1M      |
+----------------------------------------------+-------------------+--------------+
```
Usage:
 - Install packages: see script
 - Run: python aws_log_groups.py
