As we have understood how to manage IAM using Web Console, let us get into the details about managing IAM using CLI.

We should be able to manage IAM components using the aws iam command.

aws iam list-users --profile itvadmin
aws iam list-groups --profile itvadmin
aws iam list-roles --profile itvadmin
 
# Lists all AWS Managed Policies as well as custom policies
aws iam list-policies --profile itvadmin
 
# List only custom policies
aws iam list-policies --scope Local --profile itvadmin
Let us create a user itvsupport2 and assign it to the group itvsupport.

aws iam create-user --user-name itvsupport2 --profile itvadmin
aws iam list-users --profile itvadmin
 
aws iam add-user-to-group \
 --group-name itvsupport \
 --user-name itvsupport2 \
 --profile itvadmin
 
aws iam list-groups-for-user \
 --user-name itvsupport2 \
 --profile itvadmin
Let us remove the user from the group and then delete. We cannot delete the user when he is part of the group.

aws iam remove-user-from-group \
 --group-name itvsupport \
 --user-name itvsupport2 \
 --profile itvadmin
aws iam delete-user \
 --user-name itvsupport2 \
 --profile itvadmin
 
aws iam list-users --profile itvadmin