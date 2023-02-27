from Crypto.Cipher import AES
from collections import Counter
from textwrap import wrap

# because each hex digit is a 4-bit size, the block_size (16 byte) will be 32
block_size = 32

# takes one or several ciphertexts of exactly 16 byte blocks without padding as input
# and each line of ciphertext is divided on these blocks to determine if repetition occurs.
# Returns the number of total repetitions detected (count).
def countRepetitions(ciphertext):
    count = 0
    hex_text = 'No ciphertext was encrypted using ECB mode'
    with open(ciphertext) as f:
        for lines in f.readlines():
            block_array = wrap(lines, block_size)
            # the counter will count the occurrences of each block, detects repetitions
            c = Counter(block_array)
            for i in c.values():
                if i > 1:
                    count = count + i - 1
                    hex_text = lines
    # if a repetition occurs, then the whole ciphertext is copied
    print('Ciphertext in ECB Mode - \n' + hex_text)
    return count

# This function calls countRepetitions() to determine if repetitions occur;
# If even one repetition occurs then it is determined that ECB mode was used.
def detectECBMode(ciphertext):
    x = countRepetitions(ciphertext)
    if x > 0:
        print('Repetitions - ' + str(x))
        return True
    return False

isECB = detectECBMode(r"ciphertexts.txt")
if isECB == True:
    print('ECB encrypted ciphertext has been found.')
