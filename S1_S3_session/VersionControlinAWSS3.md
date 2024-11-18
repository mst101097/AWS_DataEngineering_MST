Let us understand the details related to the versioning of the S3 Bucket. We will also configure the basic life cycle.

Login to AWS Web Console and go to S3 Management Console.

Go to the bucket (dg-retail in my case).

Click on properties and review Bucket Versioning. By default, it is suspended.

You can click on edit and enable versioning.

Why Versioning of the S3 Bucket?

We might delete the objects or update the objects in S3 accidentally. Versioning will facilitate us to recover the objects using the prior version.

Due to a bug in the code or mistake, objects might get corrupted. The corrupted files or objects can be overwritten with the prior versions of the files or objects.

Once versioning is enabled we can go to Management and add Life cycle rules. We will add a basic life cycle rule to delete previous versions older than 3 days.

Click on Management then click on Create Lifecycle Rule.

Name: Archive Old Retail Files

We can filter data by Prefix or Tag or both. In our case, we will filter by Prefix - enter retail_db. The prefix is nothing but the beginning string of the Object Key.

Under Lifecycle rule actions, choose Permanently delete previous versions of objects.

Enter 3 for the Number of days after objects become previous versions.

Click on Create rule to create the rule.

We will not be able to validate immediately. You can reload files and then validate after 3 days.