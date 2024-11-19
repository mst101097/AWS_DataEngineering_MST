Let us review different storage classes in s3. You can review the storage classes as well as the Performance Chart to get a detailed understanding of Storage Classes.

We can change the storage class while uploading files either by using s3 Management Console or AWS CLI Commands.

We can edit the storage class at the level of an object or folder. It is available under Actions.

By default the storage class is Standard. You can change to any other storage class. You should be familiar with which type of storage class should be used as per your requirements.

We can configure the storage class as part of the Replication Rule. It is useful when you are using replication for low-cost backup.

Click on edit for replication rule.

At the destination, change the storage class.

Delete on the source bucket dg-retail and upload the files again.

Refresh dg-retail-copy and validate the storage class.

We can also configure the storage class as part of the Life Cycle. Update lifecycle rule Archive Old Retail Files as follows.

Change the storage class of noncurrent versions to Glacier with 0 days.

Delete noncurrent versions after 3 days.

View all the versions by clicking on List Versions.

It might not be affected immediately.