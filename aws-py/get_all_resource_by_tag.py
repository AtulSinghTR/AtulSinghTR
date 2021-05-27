import boto3

session = boto3.Session(profile_name='atul')
client = session.client('resourcegroupstaggingapi')

response = client.get_resources(
    TagFilters=[
        {
            'Key': 'tr:project-name',
            'Values': [
                'akk-u6111267',
            ]
        },
    ]
)

res = response['ResourceTagMappingList']
print(response[0])
with open('all_resource_by_tag.txt', mode='w') as file:
  data=[itm['ResourceARN'] for itm in res]
  file.write("\n".join(data))