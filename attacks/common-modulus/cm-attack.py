import os
from egcd import egcd
from Crypto.Util.number import long_to_bytes, GCD

def neg_exp(b, exp, n):
    # make sure exp < 0
    assert exp < 0
    # calculate the modular multiplicative inverse inv such that:
    # b * inv = 1 mod n
    inv = pow(b, -1, n)
    # compute inv^(-exp) mod n
    ans = pow(inv, exp*(-1), n)
    return ans


def common_modulus_attack(c1, e1, c2, e2, n):
  # calculate gcd(e1, e2) and the Bezout coefficients a, b such that:
  # e1 * a + e2 * b = 1
  (gcd, a, b) = egcd(e1, e2)
  # make sure gcd(e1, e2) = 1
  assert gcd == 1

  print('\n[+] GCD(e1, e2) = GCD(' + str(e1) + ', ' + str(e2) + ') =',gcd)
  print('[+] Calculating the Bezout coefficients a,b such that: ' + str(e1) + ' * a + ' + str(e2) + ' * b =',gcd, '...')
  print('[+] a =',a,'b =',b)
  # if a < 0, calculate the inverse of c1 and raise it to -a
  # else perform classic modular exponentiation (c1^a mod n)
  c1 = neg_exp(c1, a, n) if a < 0 else pow(c1, a, n)     
  c2 = neg_exp(c2, b, n) if b < 0 else pow(c2, b, n)

  # message = (c1 ^ a * c2 ^ b) mod n
  msg = c1 * c2 % n
  return msg


filename = 'rsa.secret'
filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
f = open(filepath, 'r')
lines = [int(line.strip().split('=')[1]) for line in f.readlines()]   # for each line in file, get the number after the '=' sign

(n,e1,e2,c1,c2) = (line for line in lines)    # assign values

pt_long = common_modulus_attack(c1, e1, c2, e2, n)
print ('Original message to long:', pt_long)
print ('Original message to bytes:', long_to_bytes(pt_long))