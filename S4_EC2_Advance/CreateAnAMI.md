Let us understand how we can create AMI for existing EC2 Instance’s Volume. In our case, the EC2 instance is ec2demo and we will name the image as ec2demoimage.

Go to EC2 Dashboard and then to Instances.

Select the instance for which you want to create AMI.

Go to Storage and click on the Volume.
ls
Create Snapshot for the Volume selected.

Go to Actions and click on Create Image

Creating AMI image from CLI

aws ec2 create-image \
  --instance-id i-ID \
  --name webAppAMI \
  --description "A sample AMI with pre installed apache web server"