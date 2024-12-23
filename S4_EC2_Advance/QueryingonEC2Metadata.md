Let us understand how we can get specific attributes from metadata while describing instances using aws ec2 command.

We can use --query to project the metadata related to specific attributes.

As metadata is represented as JSON, we have to specify the attribute using the fully qualified JSON Path.

Get only instance ids of all the instances.

aws ec2 describe-instances \
  --query 'Reservations[*].Instances[*].{Instance:InstanceId,Status:State.Name}' \
  --output json \
  --profile itvadmin \
  --region us-west-1