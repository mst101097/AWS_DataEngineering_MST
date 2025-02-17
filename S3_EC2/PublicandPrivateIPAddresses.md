Let us understand the concepts behind public and private IP addresses associated with AWS EC2 Instances.

Typically 2 IP Addresses and corresponding DNS aliases will be attached to each AWS EC2 Instance.

Public DNS aliases start with ec2 and Private DNS aliases start with ip.

Public DNS alias or underlying Public IP address can be used to access EC2 instances or services running on it via the internet from outside of AWS.

Private DNS alias or underlying Private IP address can be used for internal communication between EC2 instances within AWS VPC.

By default, the Public DNS alias or Public IP address is ephemeral. It means if you stop and start an EC2 instance, most likely the Public DNS alias and Public IP address will change.