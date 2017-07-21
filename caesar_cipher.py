def encrypt(msg, key):
	e_msg = ""
	for i in range(len(msg)):
		asc = ord(msg[i])
		if 64 < asc < 91:
			asc = ((asc - 65 + key) % 26) + 65
		elif 96 < asc < 123:
			asc = ((asc - 97 + key) % 26) + 97
		elif 47 < asc < 58:
			asc = ((asc - 48 + key) % 10) + 48
		e_msg += chr(asc)
	return e_msg

def decrypt(msg, key):
	d_msg = ""
	for i in range(len(msg)):
		asc = ord(msg[i])
		if 64 < asc < 91:
			asc = ((asc - 65 - key) % 26) + 65
		elif 96 < asc < 123:
			asc = ((asc - 97 - key) % 26) + 97
		elif 47 < asc < 58:
			asc = ((asc - 48 - key) % 10) + 48
		d_msg += chr(asc)
	return d_msg

print("Enter your message: ")
msg = input()
print("Enter your key: ")
key = int(input())

print("Plaintext : " + msg)
e_msg = encrypt(msg, key)
print("Encrypted : " + encrypt(msg, key))
print("Decrypted : " + decrypt(e_msg, key))