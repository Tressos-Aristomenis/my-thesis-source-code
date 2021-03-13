def byteflip(ct):
  ct_bytes = bytearray.fromhex(ct)  # convert ciphertext to bytes

  target_byte_index = 31    # change according to your target byte

  i = target_byte_index - 16
  old_ct_byte = hex(ct_bytes[i])  # get the byte at corresponding index of the previous ciphertext block

  p_old = ord('0')          # old target plaintext byte
  p_new = ord('1')          # new target plaintext byte
  flipped_ct_byte = hex(int(old_ct_byte, 16) ^ p_new ^ p_old)[2:]   # do the byte flip

  ct_bytes[i] = bytes.fromhex(flipped_ct_byte)[0] if len(flipped_ct_byte) == 2 else bytes.fromhex('0'+flipped_ct_byte)[0]   # alter the ciphertext
  
  return ct_bytes.hex()


ct = 'fd6e6751dfb8833417dac66040f9d5cecb53062bd206ac997e19e591835e765f54d6804b3a6c1c3a17b471ebc5410fb6eca310bf1c41c4e59c7ee27738576d7e'

print('Ciphertext before byte flipping :',ct)
flipped_ct = byteflip(ct)
print('Ciphertext after byte flipping  :',flipped_ct)