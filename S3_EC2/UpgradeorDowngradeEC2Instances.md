<!-- Let us understand how to upgrade or downgrade EC2 Instance using AWS Management Console. -->

Increasing Memory or CPU or both is called Upgrading the EC2 Instance.

Decreasing Memory or CPU or both is called Downgrading the EC2 Instance.

Here we are talking about vertical scaling. Upgrading or Downgrading the same instance with a different configuration is vertical scaling.

Adding more servers or removing some of the servers from a cluster of servers is called horizontal scaling. We typically talk about horizontal scaling with services like EMR, ECS, EKS, etc.

Let us go through the steps to upgrade as well as downgrade the EC2 Instance.

Login into AWS Management Console

Go to EC2 Console and choose the instance to which you want to upgrade.

Go to Instance State and stop the instance. You can also use CLI to stop the instance.

Go to Actions, then choose Instance Settings and then click on Change Instance Type.

As of now, the EC2 Instance is of type t2.micro. Let us upgrade it to t2.medium.

Start the server and login via SSH to confirm that you can log in to the server.

Once validated, you can shutdown, downgrade to t2.micro and start the server.

You can then log in once again to validate.

We can run the below commands to confirm the memory and CPU configuration from within the server.

free -h
lscpu
You can also run these commands to change the instance type using the command line.

aws ec2 stop-instances \
 --instance-id i-07c085b765f162233 \
 --profile itvadmin \
 --region us-west-1
 
aws ec2 modify-instance-attribute \
--instance-id i-07c085b765f162233 \
--instance-type t2.micro \
 --profile itvadmin \
 --region us-west-1
 
aws ec2 describe-instances \
--instance-id i-07c085b765f162233 \
 --profile itvadmin \
 --region us-west-1
 
aws ec2 start-instances \
 --instance-id i-07c085b765f162233 \
 --profile itvadmin \
 --region us-west-1