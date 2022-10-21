import boto3

policy_arn="arn:aws:iam::aws:policy/AdministratorAccess"
user_list = ["apple"]

def attach_user_policy(policy_arn, username):
    iam = boto3.client("iam")
    response = iam.attach_user_policy(
        UserName=username,
        PolicyArn=policy_arn
    )
    print(response)


def create_user(username):
    iam = boto3.client("iam")
    response = iam.create_user(UserName=username)
    print(response)

def create_access_key(username):
    iam = boto3.client("iam")
    response = iam.create_access_key(UserName=username)
    print(response['AccessKey'])

for userName in user_list:
	print(userName)
	create_user(userName)
	attach_user_policy(policy_arn,userName)
