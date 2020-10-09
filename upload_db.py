import boto3

db=boto3.resource('dynamodb')
table=db.Table('employees')
# Update the data in the employees table
table.put_item(
    Item={
        'emp_id':"2",
        'Name': "Charvik",
        'Age':"4"
    }
)
# Get the data from table.
response=table.get_item(
    Key={
        "emp_id":"1"
    }
)
print(response["Item"])