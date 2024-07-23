# EC2 Management with Boto3

## Overview

This project provides Python scripts for managing AWS EC2 instances using the Boto3 library. The scripts include functionalities to:

- Create an EC2 instance with a public address.
- Start and stop the instance based on scheduling rules.
- Test the EC2 management functionalities using unit tests.

## Prerequisites

- Python 3.6 or later
- AWS account with IAM user credentials
- Boto3 library

## Setup

1. **Clone the Repository**

   ```sh
   git clone https://github.com/yourusername/your-repository.git
   cd ec2_instance_management_using_boto3

   ```

2. Create and Activate a Virtual Environment

   # Create a virtual environment

   python -m venv venv

   # Activate the virtual environment

   # On Windows

   venv\Scripts\activate

   # On macOS/Linux

   source venv/bin/activate

3. Install Dependencies

   # Ensure you are in the virtual environment and install the required packages:

   pip install -r requirements.txt

4. Configuration
   # Update the schedule_script.py file with your AWS credentials, region, AMI ID, key pair name, subnet ID, and security group ID
   aws_access_key_id = 'YOUR_ACCESS_KEY'
   aws_secret_access_key = 'YOUR_SECRET_KEY'
   region_name = 'YOUR_REGION'

## Usage

# Scheduling EC2 Instance

To schedule the instance to start and stop based on specific days and times, uncomment the schedule_instance() line in schedule_script.py and run the script:

# Stopping and Starting the Instance

You can manually start and stop the instance using the following functions in schedule_script.py:
start_instance(instance_id)
stop_instance(instance_id)

Replace instance_id with the ID of your EC2 instance.

## Testing

# To run the unit tests for the project, use the following command:

python -m unittest test_schedule_script.py
This will execute the test cases defined in test_schedule_script.py, ensuring that the EC2 management functionalities work as expected.
