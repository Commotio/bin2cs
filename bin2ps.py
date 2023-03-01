#!/usr/bin/env python
##create powershell shellcode from raw shellcode
import sys
import os
 
if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("usage: %s file.bin outfile.txt\n" % (sys.argv[0],))
		sys.exit(0)

	file_size = os.path.getsize(sys.argv[1])

	shellcode = "[Byte[]] $buf = "
	i = 1

	with open(sys.argv[1], "rb") as inp:
		for b in inp.read():
			if i == file_size:
				shellcode+= "0x{:02x}".format(b) 
			else:
				shellcode += "0x{:02x}".format(b) + ","
			i += 1
	
	with open (sys.argv[2], "w+") as out:
		out.write(shellcode)
