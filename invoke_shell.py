import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect("ec2-35-154-48-197.ap-south-1.compute.amazonaws.com",
            username="ubuntu",
            key_filename="C:\\Users\\ts-karthik.kamathg\\Downloads\\AWS_test_SSH.pem")

channel = ssh.invoke_shell()
channel.send("sudo \n")
buffer = ""
while buffer.find("~$") < 0:
    buffer = str(channel.recv(9999))
    print(buffer)
