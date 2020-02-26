#! /usr/bin

FILE="sys_detail.txt"

/bin/cat >>$FILE << EOM
Uptime: `uptime -p`
System Version: `uname -v`
IP address: `hostname -I`
Logged in user: $USER
EOM
