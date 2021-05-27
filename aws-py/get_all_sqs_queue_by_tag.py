import boto3

session = boto3.Session(profile_name='atul')
client = session.client('resourcegroupstaggingapi')


def gen_tag_filters(tags_key_value):
    tag_filters=[]
    
    for key,val in tags_key_value.items():
        tag_filters.append(dict({'Key': key, 'Values': [val]}))
        
    return tag_filters


def get_sqs_list(token, resource_type, tags_key_value):
    
    response = client.get_resources(
    PaginationToken=str(token),    
    TagFilters=gen_tag_filters(tags_key_value),
    ResourceTypeFilters=resource_type,
    )
    
    next_token=response['PaginationToken']
    list_resource=[itm['ResourceARN'] for itm in response['ResourceTagMappingList']]
    
    return (next_token, list_resource)


token=''
next_token='start'
resource_filter=['sqs']
tags_key_value={'tr:financial-identifier': '66497'}

all_resource=[]
while next_token:
    next_token, list_resource = get_sqs_list(token, resource_filter, tags_key_value )
    token=next_token
    all_resource.extend(list_resource)
    #print(len(list_resource))
    
print(len(all_resource))

with open('all_sqs_queue_via_tag.txt', mode='w') as file:
  file.write("\n".join(all_resource))