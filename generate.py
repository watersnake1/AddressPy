import secrets
from sha3 import keccak_256
from coincurve import PublicKey
import os
import sys
from web3 import Web3

def gen_addrs(n, filename):
    with open(filename, 'w') as f:
        f.write('privkey, address\n')
        for i in range(0,n):
            line = gen_one_addr()
            f.write(f"{line[0]},{line[1]}\n")
    print(f"Generated {n} wallets")

def gen_one_addr():
    pk = keccak_256(secrets.token_bytes(32)).digest()
    ppk = PublicKey.from_valid_secret(pk).format(compressed=False)[1:]
    addr = keccak_256(ppk).digest()[-20:]
    pk_hex = str(pk.hex())
    ppk_hex = str(ppk.hex())
    addr_hex = '0x' + str(addr.hex())
    return (pk_hex, to_checksum(addr_hex))

def to_checksum(lowercase_addr):
    return Web3.toChecksumAddress(lowercase_addr)

if __name__ == "__main__":
    filename = input('enter a filename (.csv): ')
    to_generate = input('Generate how many wallets?: ')
    try:
        num = int(to_generate)
        gen_addrs(num, filename)
    except ValueError as e:
        print(e)
        print("input invalid")

