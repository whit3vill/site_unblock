import os, sys, thread, socket

BACKLOG = 1050
MAX_DATA_RECV = 8192

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind('', '8080')
s.listen(BACKLOG)

while 1:
	conn, client_addr = s.accept()
	thread.start_new_thread(proxy_thread, (conn, client_addr))

s.close()

def proxy_thread(conn, client_addr):
	request = conn.recv(MAX_DATA_RECV)

	first_line = requeest.split('\n')[0]
	line = first_line.split(' ')[1]
	if (line.find('://')):
		url = line.split('://')[1]
	else:
		url = line

	if (url.find('/')):
		webserver = url.split('/')[0]
	else:
		webserver = url

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((webserver, 80))

	dummy = 'GET / HTTP/1.1\r\nHost: test.gilgil.net\r\n\r\n'
	request = dummy + request
	s.send(request)

	while 1:
		data = s.recv(MAX_DATA_RECV)

		if (data.find('HTTP/')):
			if (data.find('404 Not Found') < 0):
				conn.send(data)
		else:
			break

	s.close()
	conn.close()
