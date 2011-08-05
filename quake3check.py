#!/usr/bin/python

__AUTHOR__      = 'Stephan GORGET'
__CONTACT__     = 'phantez AT gmail DOT com'

__NAME__        = 'quake3check.py'
__VERSION__     = 0.1
__DESCRIPTION__ = 'Use UDP port to check status of a Quake3 server'
__LICENSE__     = 'WTF Public License <http://sam.zoy.org/wtfpl/>'
__URL__         = 'http://github.com/phantez/quake3check'

import socket, sys

def response_to_dico(response, dico):
	resp_table = response.split("\\")
	resp_len = len(resp_table)
	for i in range(1,resp_len,2):
		dico[resp_table[i]] = resp_table[i+1]

def dico_print(dico):
	for k, v in dico.iteritems():
	        print "%30s => %s" % (str(k), str(v))

def interogate(ip, port,timeout):
	data1="\xff\xff\xff\xff\x02getinfo\n"
	data2="\xff\xff\xff\xff\x02getstatus\n"
	dico_server={}
	dico_server["server_ip"] = str(ip)
	dico_server["server_port"] = str(port)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.settimeout(timeout)

	try:
		sock.sendto(data1+"\n", (ip, port))
		received = sock.recv(1024)
		info = received.split("\n")[1]
		
		sock.sendto(data2+"\n", (ip, port))
		received2 = sock.recv(1024)
		status = received2.split("\n")[1]
		response_to_dico(info, dico_server)
		response_to_dico(status, dico_server)
#		dico_print(dico_server)
#		print received
#		print received2
		err = False
	except:
		err = "Timeout - Server is down or not responding"
	return dico_server, err
	

def main():
	if len(sys.argv) < 3:
		print "usage : %s <quake3 server ip> <port> [<key>]" % sys.argv[0]
	else :
		server_ip = sys.argv[1]
		server_port = int(sys.argv[2])
		dico_server, err = interogate(server_ip, server_port, 5)
		if err != False:
			print "Something went wrong : \"%s\"" % (err)
		else:
			if len(sys.argv) >= 4:
				key = sys.argv[3]
				if dico_server.has_key(key):
					print dico_server[key]
				else:
					print "the key you requested does not exist."
			else:
				dico_print(dico_server)

if __name__ == "__main__":
	main()
