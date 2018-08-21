import getpass
import sys
import telnetlib

#Get Username and Password
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

#Telnet to each switch and configure VLANs
for n in range (2,6):
    print "Telnet to host" + str(n)
    HOST = "192.168.122." + str(n)
    tn = telnetlib.Telnet(HOST)				# Telnet to the hosts (router in this case)

    tn.read_until("Username: ")
    tn.write(user + "\n")
    
	if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    tn.write("conf t\n")
	
	tn.write("router ospf 1\n")				# On router, configuring ospf
	tn.write("network 0.0.0.0 255.255.255.255 area 0\n")

	tn.write("end\n")
	tn.write("wr\n")
	tn.write("exit\n")

	print tn.read_all()
