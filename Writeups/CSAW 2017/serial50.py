from pwn import *
s = remote('misc.chal.csaw.io', 4239)
s.recvline()

results = ''

while s.can_recv(timeout=1):
	bits = s.recvline().strip()
	parity = int(bits[-2])
	sum_a = 0

	for bit in bits[1:-2]:
		sum_a += int(bit)

	if (sum_a % 2) == parity:
		print bits[1:-2]
		results += p8(int(bits[1:-2],2))
		s.sendline('1')
	else:
		s.sendline('0')

s.close()

print results
