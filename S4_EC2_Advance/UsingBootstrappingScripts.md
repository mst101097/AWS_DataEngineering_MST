Let us understand how to take care of installing additional libraries or softwares as EC2 instances are created and started for the first time.

Let’s terminate the existing ec2demo instance and create a new one with bootstrap script.

Launch EC2 instance using Ubuntu 18.04

Install Apache Web Server

Install Python3 Pip

Install AWS CLI using pip

We can use this document as reference to prepare the ec2 instance as it is launched.

#!/bin/bash
apt update -y
apt install apache2 -y
apt install python3-pip -y
python3 -m pip install awscli
Create instance using aws cli

aws ec2 run-instances \
  --image-id ami-013f17f36f8b1fefb \
  --count 1 \
  --instance-type t2.micro \
  --key-name keyname \
  --security-group-ids sg-ID \
  --user-data file://ec2_user_data.sh