import boto3

session = boto3.Session(profile_name='atul')
client = session.client('sqs')

response = client.list_queues()

#print(response)

with open('all_sqs_queue.txt', mode='w') as file:
  file.write(str("\n".join(response['QueueUrls'])))