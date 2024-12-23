<!-- Understanding EC2 Metadata -->

Let us understand details about metadata related to EC2 Instance.

All the actions that are performed while creating the instance are considered metadata.

Instance Type (Memory, CPU, and Instance Store).

Security Group

EC2 Key Pair

Private and Public IP Addresses as well as DNS Aliases

VPC and Subnet

We can get all the metadata in the form of JSON by running the describe-instances command.

Let us generate the JSON and review it to understand the structure of the metadata.

aws ec2 describe-instances \
 --profile itvadmin \
 --region us-west-1 > instances.json