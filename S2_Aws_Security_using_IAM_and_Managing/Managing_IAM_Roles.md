Roles are used to assigning the permissions on one service to another.

We typically create roles and attach policies with them.

All the permissions associated with the roles via policies will be inherited by the service when we attach a role to it.

Let us perform these tasks to understand how the roles are defined and used.

Create a role by name itvsupport and attach the AmazonS3ReadOnlyAccess to it. Make sure to choose the service as EC2 as we want to use this role to attach to the EC2 instance.

Launch EC2 instance using this role. We will be using the Amazon Linux image as it will come with AWS CLI already setup.

We don’t need to configure AWS CLI as the permissions are assigned via role to this EC2 instance.

If you provision, EC2 instance with other operating systems than Amazon Linux, then you need to install AWS CLI first.

Login to the EC2 instance and run these commands.

# This command will fail.
aws s3 rm s3://dg-retail1/retail_db/ --recursive
 
# This command should work as the role has s3 read-only access
aws s3 ls dg-retail1 --recursive