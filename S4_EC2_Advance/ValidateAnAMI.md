Once the image is created, follow these steps to validate.

Go to Images and create an instance using it.

We have to go through the standard steps.

Choosing Instance Type

Configure Instance Details

Add Storage

Add or Choose Security Group

Launch with a new or existing Key Pair.

Once the instance is launched, we will name it as ec2demo1.

Wait until the instance is started and then connect via SSH. Once you connect via SSH, make sure to validate that we have Apache 2 as well as AWS CLI already setup and also Apache 2 is started on port 80.

We can also use command line to create the instance using our AMI
<!-- 
aws ec2 run-instances \
  --image-id ami-ID \
  --count 1 \
  --instance-type t2.micro \
  --key-name keyname \
  --security-group-ids sg-ID -->