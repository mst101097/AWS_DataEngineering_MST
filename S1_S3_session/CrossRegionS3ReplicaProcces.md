AWS S3 Cross-Region Replication for fault tolerance
Let us go through the details about the Cross-Region Replication of s3 Bucket or objects within s3 Bucket.

In some extreme cases, our S3 might not be accessible within a specific region due to unforeseen circumstances which might impact data centers in AWS Region or AZ within AWS Region.

By enabling Cross-Region Replication we can have a copy of the s3 bucket or objects within the bucket in some other Region.

Let’s enable Cross-Region Replication of our bucket dg-retail.

Login to AWS Web Console and go to S3 Management Console.

Create another bucket in another region by name dg-retail-copy

Create a role by the name AWSS3FullAccessRole with AmazonS3FullAccess policy.

Go to the bucket (dg-retail in my case).

Click on Management and go to Replication rules.

Click on Create replication rule.

Replication rule name: Retail replication

Status: Enabled

Choose a Rule Scope: Choose to Limit the scope of this rule using one or more filters

Prefix: retail_db (all objects under retail_db will be replicated)

Enter bucket name: dg-retail-copy

Make sure to enable versioning on the destination bucket.

Make sure to choose AWSS3FullAccessRole and click on Save.

Note: Only new files added with Prefix defined in the filter will be replicated. Existing files will not be replicated.