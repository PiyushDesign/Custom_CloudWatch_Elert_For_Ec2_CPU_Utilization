import json
import boto3
import datetime

# Initialize the Boto3 clients
cloudwatch_client = boto3.client('cloudwatch', region_name='ap-south-1')
sns_client = boto3.client('sns', region_name='ap-south-1')

# Constants
INSTANCE_ID = 'i-06b205998588d9c99'  # Your EC2 instance ID
SNS_TOPIC_ARN = 'arn:aws:sns:ap-south-1:533267114782:AlarmNotificationTopic'  # Your SNS topic ARN

def lambda_handler(event, context):
    # Get CPU utilization
    cpu_utilization = get_cpu_utilization(INSTANCE_ID)

    # Construct the subject and message body
    subject = f"Your Server's CPU is {cpu_utilization}%. Please check"
    message = f"""
    Hi,

    The server CPU usage is high. Please check.

    Instance ID: {INSTANCE_ID}
    CPU Utilization: {cpu_utilization}%
    """

    # Publish the message to SNS
    response = sns_client.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=message.strip(),
        Subject=subject
    )

    return {
        'statusCode': 200,
        'body': json.dumps('CPU Utilization notification sent to SNS!')
    }

def get_cpu_utilization(instance_id):
    # Get the CPU utilization metric from CloudWatch
    response = cloudwatch_client.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[{
            'Name': 'InstanceId',
            'Value': instance_id
        }],
        StartTime=datetime.datetime.utcnow() - datetime.timedelta(minutes=10),
        EndTime=datetime.datetime.utcnow(),
        Period=300,
        Statistics=['Average']
    )
    
    # Get the average CPU utilization and convert to integer
    if len(response['Datapoints']) > 0:
        return int(round(response['Datapoints'][0]['Average']))  # Round and convert to int
    return 0  # Return 0 if no data points are available
