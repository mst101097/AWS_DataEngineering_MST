Go to AWS Web Console and then go to EC2 Console.

Go to Elastic IPs under Network & Security.

Click on Allocate Elastic IP address to lease the IP address so that we can associate with the ec2 instance created earlier.

Select newly allocated elastic IP address, go to Actions and click on Associate Elastic IP address.

Select the EC2 instance in the drop-down related to Instance.

Now validate by running SSH using newly associated Public DNS Alias and make sure that you can connect to EC2 instance.

You can also try accessing Apache Web Server that is supported earlier via http.