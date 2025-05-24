
import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
    ImageId='956c7d316',  # Amazon Linux 2 (us-east-1 region)
    InstanceType='t2.micro',
    MinCunt=1,
    MaxCount=1
)
