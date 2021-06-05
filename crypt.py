#!/bin/env python3	
import base64
import sys

INP = sys.argv

del INP[0]

def encrypt(plain, XORS):
	cipher = ''

	for c in plain:
		s = c
		for xor in XORS:
			s = chr((ord(s) ^ xor ))
		cipher += s
	# Raw Cipher
	cipher = cipher.encode("ASCII")
	for i in range(int(len(XORS))):
		cipher = base64.b64encode(cipher)
	print("Hard Cipher =>", cipher.decode("ASCII"))


def decrypt(cipher, XORS):
	cipher = cipher.encode("ASCII")

	# Hard Cipher To Raw Cipher

	for i in range(int(len(XORS))):
		cipher = base64.b64decode(cipher)
	# Raw Cipher To String

	cipher = cipher.decode("ASCII")
	plain = ''

	for c in cipher:
		s = c
		for xor in XORS:
			s = chr((ord(s) ^ xor ))
		plain += s
	print("Plain => ", plain)



# encrypt('ermia M')
# decrypt('U2xSSmRFdFRSbWRFVVQwOQ==')

def main(method, data, XORS):
	for i in range(len(XORS)):
		XORS[i] = int(XORS[i])

	if method == 'en':
		encrypt(data, XORS)
	elif method == 'de':
		decrypt(data, XORS)
	else:
		print("Usage\n\t Encrypt => ./crypt.py en <String> <Xors>\n\t Decrypt => ./crypt.py de <Encryptrd> XORS\nE.G. $ ./crypt.py en ermia 51 54 65 51 54 51 51")

if __name__ == '__main__':
	try:
		main(INP[0], INP[1], INP[2:])
	except:
		print("Usage\n\t Encrypt => ./crypt.py en <String> <Xors>\n\t Decrypt => ./crypt.py de <Encryptrd> XORS\nE.G. $ ./crypt.py en ermia 51 54 65 51 54 51 51")