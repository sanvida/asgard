import boto3
from datetime import datetime
import time
import os

# Initialize a session using Amazon EC2
session = boto3.Session(
    aws_access_key_id = os.getenv('aws_access_key_id'),
    aws_secret_access_key = os.getenv('aws_secret_access_key'),
    region_name = os.getenv('region_name')
)

# Initialize the EC2 resource
ec2 = session.resource('ec2')

# Specify your EC2 instance ID
INSTANCE_ID = os.getenv('INSTANCE_ID')

def start_instance(instance_id):
    """
    Starts the EC2 instance.
    If the instance is already running, it does nothing.
    """
    instance = ec2.Instance(instance_id)
    if instance.state['Name'] != 'running':
        instance.start()
        instance.wait_until_running()  # Wait until the instance is in the running state
        print(f"Started instance {instance_id}")
    else:
        print(f"Instance {instance_id} is already running")

def stop_instance(instance_id):
    """
    Stops the EC2 instance.
    If the instance is already stopped, it does nothing.
    """
    instance = ec2.Instance(instance_id)
    if instance.state['Name'] != 'stopped':
        instance.stop()
        instance.wait_until_stopped()  # Wait until the instance is in the stopped state
        print(f"Stopped instance {instance_id}")
    else:
        print(f"Instance {instance_id} is already stopped")

def schedule_instance():
    """
    Schedule the instance to run on alternate days (Monday, Wednesday, Friday, Sunday)
    between 9:00 AM GMT to 11:30 AM GMT. Ensure the instance remains stopped during the
    remaining time.
    """
    while True:
        try:
            now = datetime.utcnow()
            current_day = now.strftime('%A')
            current_time = now.time()

            # Define the allowed days and time window
            allowed_days = ['Monday', 'Wednesday', 'Friday', 'Sunday']
            start_time = datetime.strptime('09:00:00', '%H:%M:%S').time()
            end_time = datetime.strptime('11:30:00', '%H:%M:%S').time()

            # Check if today is a valid day to run the instance
            if current_day in allowed_days:
                # Check if current time is within the allowed time window
                if start_time <= current_time <= end_time:
                    start_instance(INSTANCE_ID)
                else:
                    stop_instance(INSTANCE_ID)
            else:
                stop_instance(INSTANCE_ID)

            # Sleep until the next minute to avoid excessive API calls
            time.sleep(60)

        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(60)  # Wait a minute before retrying to avoid rapid looping on errors

# Schedule the instance management
schedule_instance()
