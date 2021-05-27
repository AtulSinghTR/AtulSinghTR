import boto3

session = boto3.Session(profile_name='atul')
client = session.client('resourcegroupstaggingapi')

def gen_tag_filters(tags_key_value):
    tag_filters=[]
    _ = [tag_filters.append(dict({'Key': key, 'Values': [val]})) for key,val in tags_key_value.items()]
    return tag_filters


def get_resource_list(resource_type, tags_key_value):
    
    response = client.get_resources(
                            TagFilters=gen_tag_filters(tags_key_value),
                            ResourceTypeFilters=resource_type,
                            ResourcesPerPage=99
    )

    list_resource=[itm['ResourceARN'] for itm in response['ResourceTagMappingList']]

    while 'PaginationToken' in response and response['PaginationToken']:
        response = client.get_resources(
                            PaginationToken=response['PaginationToken'],    
                            TagFilters=gen_tag_filters(tags_key_value),
                            ResourceTypeFilters=resource_type,
                            ResourcesPerPage=99
        )
        
        list_resource.extend([itm['ResourceARN'] for itm in response['ResourceTagMappingList']])
            
    return list_resource



def main():

    resource_filter=['sqs', 'ec2', 's3']
#    tags_key_value={'tr:financial-identifier': '66497', 'tr:project-name': 'akk-u6111267'}
    tags_key_value={'tr:financial-identifier': '66497'}


    all_resource = get_resource_list(resource_filter, tags_key_value)
        
    print(f"Total_Resources: {len(all_resource)}")
    out_file_name='all_Arns_'+'_'.join(resource_filter)+'_resource.txt'
    data="\n".join(all_resource)#.replace(':', ',')
    
    with open(out_file_name, mode='w') as file:
        #file.write('ResourceType,Region,AccountId,ResourceName\n')
        file.write(data)
    

if __name__ == '__main__':
    main()