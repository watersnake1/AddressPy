import os

# PK tuple - a simple function that turns a private key into an array of four 64 bit parts
# This is intended for use with ECDSA and EDDSA zk circuits, which sometimes used chunked private keys
# Enter the private key as a 64 bit hex number
def make_pk_tuple(pk_in):
    pk_in = int(pk_in, 16)
    mod = 2 ** 64
    out = [0,0,0,0]
    temp = pk_in

    for i in range(0,len(out)):
        out[i] = temp % mod
        temp = temp // mod
    return out

if __name__ == "__main__":
    pk = input("enter pk:")
    tup = make_pk_tuple(pk)
    print(tup)
