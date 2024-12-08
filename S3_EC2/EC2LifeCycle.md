Let us go through the life cycle of EC2 Instance. EC2 instance will be in one of these states as long as it is not terminated.

Running

Stopped

Restarting

If you stop the EC2 instance, the public IP might be reset as it is ephemeral by default. You need to lease elastic IP and assign it to the EC2 instance so that public IP does not change.

As long as EC2 Instance is stopped you will not be charged for the instance. But, if you use EBS for storage, you have to pay for it.