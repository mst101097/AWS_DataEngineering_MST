We can provide finer granular permissions on any AWS Service or component using Custom Policies. Let us do a lab to understand how we can use custom policies to grant specific permissions to a user on a specific bucket.

Go to Policies and click on Create Policy. We will be using ITVSupportS3RetailDBAll as the name for the policy.

We can enter the service and use the wizard to create the policy or we can import from managed policies and improvise on top of it.

Let us import AmazonS3ReadOnlyAccess and then customize it. We will give the get, put and delete permissions on the retail_db folder in the dg-retail1 bucket along with list all buckets permission.

{
 "Version": "2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:*"
 ],
 "Resource": "arn:aws:s3:::dg-retail1/retail_db*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:List*"
 ],
 "Resource": "*"
 }
 ]
}
Once the policy is created, detach the existing policy from the itvsupport group and attach the new policy.

You can validate by running the below commands. We should be able to delete and copy the files again using the itvsupport1 profile as itvsupport1 is part of the itvsupport group.

aws s3 rm s3://dg-retail1/retail_db/ --recursive --profile itvsupport1
 
aws s3 cp ~/Research/data/retail_db s3://dg-retail1/retail_db/ \
 --recursive \
 --exclude "*.sql" \
 --exclude "README.md" \
 --profile itvsupport1
 
aws s3 ls dg-retail1 --recursive --profile itvsupport1
 
# This command should fail
aws s3 mb s3://dg-retail2 --profile itvsupport1