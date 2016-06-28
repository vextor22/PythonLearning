import socket
socket.setdefaulttimeout(2)

s = socket.socket()
s.connect(("matthewhiggins.org",22))
ans = s.recv(1024)
print(ans)