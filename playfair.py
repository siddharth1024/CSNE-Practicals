def create_matrix():
	return [[0]*5 for i in range(5)]

def print_matrix(m):
	for i in range(5):
		for j in range(5):
			print(m[i][j],end=" ")
		print()

def exists(word, letter):
	for i in range(len(word)):
		if word[i] == letter and letter != 'J':
			return True
	return False

def search_in_matrix(m, l):
	for i in range(5):
		for j in range(5):
			if m[i][j] == l:
				return [i, j]
	return -1

def playfair(msg, key):
	asc = 65
	m = create_matrix()

	for c in range(25):
		i = int(c / 5)
		j = int(c % 5)

		if c < len(key):
			m[i][j] = key[c]
		else:
			while exists(key,chr(asc)) == True:
				asc += 1
			if chr(asc) == 'J':
				asc += 1
			m[i][j] = chr(asc)
			asc += 1

	f = []
	for c in range(len(msg)):
		if msg[c] == " ":
			continue
		if len(f) > 0 and f[-1] == msg[c]:
			f.append("X")
		f.append(msg[c])

	if len(f) % 2 == 1:
		f.append("X")

	for c in range(1, len(f), 2):
		print(f[c-1]+f[c], end=" ")

	print()

	for c in range(1, len(f), 2):
		a = search_in_matrix(m, f[c-1])
		b = search_in_matrix(m, f[c])
		if a != -1 and b != -1:
			if a[0] == b[0]:
				x = m[b[0]][b[1]]
				y = m[b[0]][(a[1]+2)%5]
			elif a[1] == b[1]:
				x = m[(b[0]+2)%5][b[1]]
				y = m[a[1]][(b[0]+1)%5]
			else:
				x = m[a[0]][b[1]]
				y = m[b[0]][a[1]]
			print(x+y, end=" ")

	print()
	return m


print_matrix(playfair("HIDE THE GOLD IN THE TREE STUMP","PLAYFIREXM"))
