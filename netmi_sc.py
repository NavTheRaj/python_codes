
from netmiko import ConnectHandler,FileTransfer

router ={
        'device_type'= "juniper",
        'ip' = "12.0.1.28",
        'username'= "rviews",
        'password'= "rviews",
        }

try:
    ssh_conn=ConnectHandler(**router)
    ssh_conn.enable()

    command1="show bgp summary"
    output=ssh_conn.send_command(command1)
    with open("log_ssh.txt","w") as f:
        f.write(output1)


except:
    print("Device not found")

