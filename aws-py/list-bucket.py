import boto3, pathlib
import ConfigParser

def read_config_file(file_name, section):
  # Reading config file
  config_file_name=pathlib.Path.cwd() / file_name  
  config = ConfigParser.ConfigParser()
  config.read(config_file_name)
  return config.items(section)


cnf=read_config_file('config.cfg')
proj_abr=cnf['proj_abr']
print(proj_abr)

# session = boto3.Session(profile_name='atul')
# s3_client = session.client('s3')
# resp=s3_client.list_buckets()

# #print(resp.keys())
# #print(resp['Buckets'])

# all_bucket_names=[]
# _=[all_bucket_names.append(itm['Name']) for itm in resp['Buckets'] if proj_abr in itm['Name']]
  

# print(all_bucket_names)
  


# con = boto3.client('s3', aws_access_key_id='my_aws_access_key',
#                   aws_secret_access_key='my_aws_secret_key',
#                   region_name=os.environ.get('AWS_DEFAULT_REGION'))