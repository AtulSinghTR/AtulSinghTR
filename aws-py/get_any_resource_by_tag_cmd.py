import boto3
import argparse


session = boto3.Session(profile_name='atul')
client = session.client('resourcegroupstaggingapi')
    
    
def input_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tags", required=True,
                        help="tag key value pair (eg, --tags \"tr:financial-identifier=66497\")")
    parser.add_argument("--resource", required=True,
                        help="AWS resource array (eg, --resource 'sqs,ec2,s3')")    
    return parser.parse_args()

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
    
    # reading parameters
    args = input_args()
    
    tags_key_value={}
    resource_filter=args.resource.split(',')
    for data in args.tags.split(','):
        k=str(data.split('=')[0]).strip()
        v=str(data.split('=')[1]).strip()
        tags_key_value[k] = v
    
    #print(args.tags, tags_key_value)


    all_resource= get_resource_list(resource_filter, tags_key_value)
        
    print(f"Total_Resources: {len(all_resource)}")
    out_file_name='all_Arns_'+'_'.join(resource_filter)+'_resource'
    data="\n".join(all_resource)
    
    with open(out_file_name+'.txt', mode='w') as file:
        file.write(data)
        
    with open(out_file_name+'.csv', mode='w') as file:
        file.write('_,_,ResourceType,Region,AccountId,ResourceName\n')
        file.write(data.replace(':',','))   

if __name__ == '__main__':
    main()