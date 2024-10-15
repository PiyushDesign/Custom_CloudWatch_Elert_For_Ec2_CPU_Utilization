# Task: When CPU utilisation reach to 50% then customised email should be sent to the Email with the detail of the instance id and CPU utilization.

# Create Instance:

```sh
    Create an Instance.
```

# Step 1: Create Lambda
``` sh
    Go to the AWS Lambda console.

    Create a new function:

    Click Create function.
    Choose Author from scratch.
    Provide a name (e.g., SendAlarmNotification).
    Select a runtime (e.g., Python 3.x).
    Set the permissions (create a new role with basic Lambda permissions).
    Click Create function.
    Add code to send a notification: Here’s an example code snippet that you can use in your Lambda function:
```

# Step 2: Create SNS and Subscribe it

```sh

    Go to the Amazon SNS Console:

    Navigate to the Amazon SNS Console.
    Create a Topic:

    Click on Topics in the left sidebar.
    Click on Create topic.
    Select Standard as the topic type.
    Enter a name for the topic (e.g., CpuUtilizationAlerts).
    Click Create topic.
    Note the Topic ARN for later use.

    Subscribe Your Email to the SNS Topic

    Open the Topic:
    Click on the topic you just created (e.g., CpuUtilizationAlerts).

    Create a Subscription:

    Click on Create subscription.
    In the Protocol dropdown, select Email.
    In the Endpoint field, enter the email address where you want to receive notifications.
    Click Create subscription.
    Confirm the Subscription:

    Check your email for a subscription confirmation from Amazon SNS and confirm the subscription by clicking the link provided in the email.

```

# Step 3: Cloud watch Alarm:

```sh
    Go to the CloudWatch Console:

    Navigate to the Amazon CloudWatch Console.

    Create an Alarm:

        Click on Alarms in the left sidebar.
        Click Create Alarm.
        Choose Select metric.

    Navigate to EC2 > Per-Instance Metrics, and select CPUUtilization for your instance.

        Click Select metric.
        
    Set the Alarm Conditions:
    Set the threshold (e.g., Greater than 50% for 1 consecutive period of 5 minutes).
    
    Click Next.

    Configure Actions:

        Under Configure actions, select Lambda function.
        Choose your Lambda function (CPUMonitorFunction) from the dropdown.

    Review and Create the Alarm:

    Click Next, review your settings, and click Create alarm.
```

# Step 4: Lambda Permission Settings

```sh

    In the AWS Lambda Console, navigate to your function’s configuration.
    Under the Permissions section, find Resource-based policy statements.
    Select Add permissions and choose AWS service.
    Select Other from the dropdown list.
    Add a unique statement ID for tracking.
    For Principal, add lambda.alarms.cloudwatch.amazonaws.com.
    Under Source ARN, add the ARN of your CloudWatch alarm.
    In the Action dropdown, select lambda:InvokeFunction.
    Click Save to apply the changes.

```

# Step 5: Increase the CUP utilization in Instance using Python script

```sh

    In AWS instance, Create a python file : cpu-utilization.py
    Add the code from the "Increase CPU utilization.py" and pase it to cpu-utilization.py

    Now run the File using python3 cpu-utilization.py

```
