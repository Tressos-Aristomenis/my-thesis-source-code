import os

# Source : https://stackoverflow.com/questions/9916334/bits-to-string-python

def bits2str(b):
    return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(b)]*8))

def str2bits(s):
    return [int(i) for i in (''.join(format(ord(c), '08b') for c in s))]
# --------------------------------------------------------------------------

################ SCENARIO INSPIRED BY ################
##############    https://inssec.dev    ##############
######################################################

def generate_keystream(pt_bits, seed):
    keystream = []
    state = seed    # initialize state with seed
    for j in range(len(pt_bits)):
        keystream.append(state[15])     # the last bit of the state is appended to the keystream
        val = ((((state[15]^state[13])^state[12])^state[11])^state[9])^state[6]     # LFSR XOR 
        state = [val] + state[0:15]     # update state

    return keystream

# decrypt 'ct_bits' with 'keystream'
def decrypt(ct_bits, keystream):
    pt_bits = ''
    for i in range(len(ct_bits)):
        p_bit = int(ct_bits[i]) ^ keystream[i]
        pt_bits += str(p_bit)

    return pt_bits


filename = 'creds.txt'
filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
f = open(filepath, 'r')

ct_bits = f.readline().strip()

prefix = 'ssh'
prefix_bits = str2bits(prefix)

# xor the first 16 bits of ciphertext with the first 16 bits of plaintext (ss)
# we want 16 bits because the length of the LFSR is 16
first16_keystream_bits = [a ^ b for a, b in zip(prefix_bits, [int(i) for i in ct_bits[:16]])]

seed = [i for i in reversed(first16_keystream_bits)]    # the seed is the first 16 keystream bits in reverse order
keystream = generate_keystream(ct_bits, seed)
pt_bits = decrypt(ct_bits, keystream)
print('\nPlaintext bits:',pt_bits)
print('Original message:',bits2str(pt_bits))