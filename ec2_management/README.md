# EC2 Management with Boto3

## Overview

This project provides Python scripts for managing AWS EC2 instances using the Boto3 library. The scripts include functionalities to:

- Start and stop the instance based on scheduling rules.
- Test the EC2 management functionalities using unit tests.

## Prerequisites

- Python 3.6 or later
- AWS account with IAM user credentials
- Boto3 library

## Setup

1. **Clone the Repository**

   ```sh
   git clone https://github.com/sanvida/asgard.git
   cd ec2_management
   ```

2. **Create and Activate a Virtual Environment**

   I. Create a virtual environment

   ```python
   python -m venv venv
   ```

   II. Activate the virtual environment

   **On Windows**

   ```python
   venv\Scripts\activate
   ```
   
   **On macOS/Linux**
   ```sh
   source venv/bin/activate
   ```

3. **Install Dependencies**

   Ensure you are in the virtual environment and install the required packages:
   ```python
   pip install -r requirements.txt
   ```

4. **Configuration**
   Update the schedule_script.py file with your AWS credentials
   ```python
   aws_access_key_id = 'YOUR_ACCESS_KEY'
   aws_secret_access_key = 'YOUR_SECRET_KEY'
   region_name = 'YOUR_REGION'
   ```

## Usage

### Scheduling EC2 Instance

To schedule the instance to start and stop based on specific days and times as mentioned in the code, run the script:

```python
python schedule_script.py
```

### Stopping and Starting the Instance

You can manually start and stop the instance using the following functions in schedule_script.py:

```python
start_instance(instance_id)
stop_instance(instance_id)
```
Replace instance_id with the ID of your EC2 instance.

## Testing
To run the unit tests for the project, use the following command:

```python
python -m unittest test_schedule_script.py
```
This will execute the test cases defined in test_schedule_script.py, ensuring the EC2 management functionalities work as expected.

## Using GitHub Codespaces

1. **Open in Codespaces**: Click the "Code" button on the GitHub repository page and select "Open with Codespaces" to create a new Codespace.
2. Change the directory
   ```bash
   cd ec2_management
   ```
3. **Install Dependencies**: Once the Codespace is set up, run the following commands in the terminal to install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the ec2 management script:
    ```python
   python schedule_script.py
   ```
5. Testing
   Run the tests using unittest:
   ```python
   python -m unittest test_schedule_script.py
   ```
