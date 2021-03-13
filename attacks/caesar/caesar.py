################ INSPIRED BY ################
#   https://github.com/AndyStabler/Crypto   #
#############################################



import operator
import re

# English letters' probability of occurence in a text
freqs = [
    ('A', 0.0816699), ('B', 0.01492), ('C', 0.02782), ('D', 0.04253), ('E', 0.12702),
    ('F', 0.02228), ('G', 0.02015), ('H', 0.06094), ('I', 0.06966), ('J', 0.00153),
    ('K', 0.00772), ('L', 0.04025), ('M', 0.02406), ('N', 0.06749), ('O', 0.07507),
    ('P', 0.01929), ('Q', 0.00095), ('R', 0.05987), ('S', 0.0632699), ('T', 0.0905599),
    ('U', 0.02758), ('V', 0.00978), ('W', 0.0236), ('X', 0.0015), ('Y', 0.01974), ('Z', 0.00074)
]

# decrypt 'ct' using 'key'
def decrypt(key, ct):
    message = ct.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in ct:
        if letter in alpha:
            letter_index = (alpha.find(letter) - key) % len(alpha)
            result += alpha[letter_index]
        else:
            result += letter
    return result

# calculate the chi-squared value of 'pt'
def chi_squared(pt):
    C = count_chars(pt);
    
    cs = 0.0;
    for i in range(26):
        expected = len(pt) * freqs[i][1]
        cs += pow(C[i] - expected, 2) / expected;
        
    return cs;

# count the number of occurences of each letter in 'text'
def count_chars(text):
    counts = [0] * 26;

    for c in text:
        if c.isalpha():
            counts[ord(c) % 65 - ord('A') % 65] += 1;
            
    return counts;

# calculate all shifts and store them to dictionary along with their equivalent chi-squared value
# sort the dict by chi-squared value in ascending order and return it
# the first element is our best guess of the shift
def calculate_all_shifts(ct):
    d = {}
    
    for k in range(26):
        decrypted = decrypt(k, ct)
        cs = chi_squared(decrypted)
        d[k] = cs
    
    return sorted(d.items(), key=operator.itemgetter(1))
    
ct = "ESP PYNCJAETZY DEPA APCQZCXPO MJ L NLPDLC NTASPC TD ZQEPY TYNZCAZCLEPO LD ALCE ZQ XZCP NZXAWPI DNSPXPD, DFNS LD ESP GTRPYÈCP NTASPC, LYO DETWW SLD XZOPCY LAAWTNLETZY TY ESP CZE13 DJDEPX. LD HTES LWW DTYRWP-LWASLMPE DFMDETEFETZY NTASPCD, ESP NLPDLC NTASPC TD PLDTWJ MCZVPY LYO TY XZOPCY ACLNETNP ZQQPCD PDDPYETLWWJ YZ NZXXFYTNLETZYD DPNFCTEJ."

ct = ct.upper()
replaced_ct = re.sub('[^a-zA-Z]+', '', ct).upper()

if __name__ == "__main__":
    shifts = calculate_all_shifts(replaced_ct)
    
    print()
    
    # for key, cs in shifts:
    #     tmp = str(key) if key > 9 else "0" + str(key)
    #     print(" plaintext:",decrypt(key, ct),"| key:",tmp,"| chi-squared:",cs)
    
    best_shift = shifts[0][0]
    print('-' * 40)
    print('Potential key :', best_shift)
    print('-' * 40)
    print('Chi-Squared value :', shifts[0][1])
    print('-' * 40)
    print('Ciphertext :', ct)
    print('-' * 40)
    print('Plaintext :', decrypt(best_shift, ct))
    print('-' * 40)     
        


    
    
