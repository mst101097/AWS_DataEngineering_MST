Let us understand IAM Identity-based Policies. We will be focusing on Predefined policies for now.

Permissions are assigned to policies using JSON Syntax.

Policies are typically attached to either group or role. It is also possible to attach policies directly to users.

Users, groups, and roles are also known as IAM identities.

We can attach more than one policy to an IAM identity.

We have predefined policies which we can leverage and also we can define custom policies.

Let us review the following policies to understand how permissions on services are typically defined.

AmazonS3FullAccess

AmazonS3ReadOnlyAccess

Here are the key terms which you should be familiar with related to policies.

Effect - This is where you typically define Allow or Deny

Action - This is where you typically define the type of actions that can be performed

Resource - We can control the permissions over the resources that are related to the Effect.

For example:

Effect - s3 (service)

Action - Get, List, Put, Delete, etc.

Resource - Buckets or objects within the bucket we have created.

Let us perform a few tasks related to Identity-based Policies.

Create a new user itvsupport1 with only programmatic access.

Configure AWS CLI with profile itvsupport1.

Attach AmazonS3ReadOnlyAccess to itvsupport1.

Make sure a bucket is created using AWS Web Console by logging in as admin or root user. I will be creating a bucket by the name dg-retail. If you already have such a bucket, you can directly copy files into S3.

Try running this command to copy files into the bucket.

aws s3 cp ~/Research/data/retail_db s3://dg-retail1/retail_db/ \
 --recursive \
 --exclude "*.sql" \
 --exclude "README.md" \
 --profile itvsupport1