Let us understand how we can filter the data while describing instances using aws ec2 command.

Get all the ec2 instances which are of type t2.micro

aws ec2 describe-instances \
 --filters Name=instance-type,Values=t2.micro \
 --output json \
 --profile itvadmin \
 --region us-west-1
Get only instance id, type and status of t2.micro instances.

aws ec2 describe-instances \
 --filters Name=instance-type,Values=t2.micro \
 --query 'Reservations[*].Instances[*].{Instance:InstanceId,InstanceType:InstanceType,Status:State.Name}' \
 --output json \
 --profile itvadmin \
 --region us-west-1
Get only instance id, type and status of t2.micro instances in stopped state.

aws ec2 describe-instances \
 --filters Name=instance-type,Values=t2.micro Name=instance-state-name,Values=stopped \
 --query 'Reservations[*].Instances[*].{Instance:InstanceId,InstanceType:InstanceType,Status:State.Name}' \
 --output json \
 --profile itvadmin \
 --region us-west-1