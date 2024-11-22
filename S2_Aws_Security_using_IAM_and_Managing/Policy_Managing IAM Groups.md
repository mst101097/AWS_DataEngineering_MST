
Let us go through the details related to IAM Groups.

We typically have users in IAM Groups.

Permissions are typically defined using Policies and policies are assigned to Groups.

All the users in the group will inherit all the permissions associated with the group.

Let us perform these tasks to make sure that we are comfortable in dealing with groups.

Let us create two groups.

itvadmin

itvsupport

Add user itvadmin to group itvadmin

Add user itvsupport1 to group itvsupport

Detach AdministratorAccess policy from user itvadmin and attach it to group itvadmin

Detach AmazonS3ReadOnlyAccess policy from user itvsupport1 and attach it to group itvsupport

Run the below command as an itvadmin user to confirm that the user account has all the admin permissions that were assigned earlier directly.

aws s3 rm s3://dg-retail1/retail_db/ --recursive --profile itvadmin
 
aws s3 cp ~/Research/data/retail_db s3://dg-retail1/retail_db/ \
 --recursive \
 --exclude "*.sql" \
 --exclude "README.md" \
 --profile itvadmin
Run the below commands as itvsupport1 to confirm that the user account has only read-only access on s3.

# Both these commands will fail.
aws s3 rm s3://dg-retail1/retail_db/ --recursive --profile itvsupport1
 
aws s3 cp ~/Research/data/retail_db s3://dg-retail1/retail_db/ \
 --recursive \
 --exclude "*.sql" \
 --exclude "README.md" \
 --profile itvsupport1
 
# This command should work as the user have s3 read-only access
aws s3 ls dg-retail1 --recursive --profile itvsupport1