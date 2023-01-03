#!/usr/bin/python3

"""Print the ASCII alphabets in lowercase except q and e """
for letter in range(97, 123):
	if chr(letter) != 'q' and chr(letter) != 'e':
		print("{}".format(chr(letter)), end="")
