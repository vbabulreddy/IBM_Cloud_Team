""" 1. How to connect ec2 instance using ssh """

import boto3
import botocore
import paramiko

key = paramiko.RSAKey.from_private_key_file(path/to/mykey.pem)
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

""" Connect/ssh to an instance """
try:

    """ Here 'ubuntu' is user name and 'instance_ip' is public IP of EC2 """
    client.connect(hostname=instance_ip, username="ubuntu", pkey=key)

    """ Execute a command(cmd) after connecting/ssh to an instance """
    stdin, stdout, stderr = client.exec_command(cmd)

    print(stdout.read())

    """ close the client connection once the job is done """
    client.close()

except Exception as e:
    print(e)

""" for more information: https://stackoverflow.com/questions/42645196/how-to-ssh-and-run-commands-in-ec2-using-boto3 """

