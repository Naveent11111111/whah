
import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
    ImageId='ami-0c02fb55956c7d316',  # Amazon Linux 2 (us-east-1 region)
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1
)
