ssh -i ~/.ssh/add pem file name\
 ubuntu@ec2-34-232-68-20.compute-1.amazonaws.com
 
 
 
Security Groups Basics
------------------------
Let us understand the basics of security groups. AWS EC2 Security Groups facilitate us to define Firewall rules to block unintended traffic into EC2 instances from external systems.

We need to choose an existing security group or create a new one while launching an ec2 instance.

By default, SSH Daemon will be running on Linux-based ec2 instances on AWS using port 22.

The default rule as part of most of the security groups is to open port 22 so that we can connect from remote machines using SSH.

We will be able to login using SSH only.

Let us perform these tasks to understand the relevance of security groups.

Make sure you can connect to the instance that is launched earlier using SSH.

Go to the security group associated with the ec2 instance and delete the rule related to port 22.

Try connecting to the ec2 instance using SSH. It will be struck.

Go back and open port 22 for everyone and validate by using SSH.

Install Apache on the Ubuntu machine. Login and run these commands to install and start the Apache Web server.

sudo apt update
sudo apt install -y apache2
sudo systemctl status apache2
# Hit Ctrl+C to come out of the command output
 
# Confirm that the apache server is running on port 80 using telnet
telnet localhost 80
telnet ec2-34-232-68-20.compute-1.amazonaws.com 80
Go to the browser and try to access Apache Web Server using http://<public_ip>. Here is the link for your reference - http://ec2-34-232-68-20.compute-1.amazonaws.com

The link will not work. Now go to the security group and the new rule for port number 80 using My IP.

Now the link should work without any issues. It will launch the default Apache Web Server Page for Ubuntu.