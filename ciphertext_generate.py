from Crypto.Cipher import AES

# this plaintext contains 16 byte blocks, where some are repeated.
plaintext = b'this sentence is intended to be used against humanity and I say this sentence is pretty dumb but intended to be just a joke! or is it? maybe not'
key = b'mysupersecretkey'

# plaintext will be encrypted with the provided key using these three different methods.
# each encryption mode will be written to a line to the local ciphertexts.txt document.
ECB_cipher = AES.new(key, AES.MODE_ECB)
CBC_cipher = AES.new(key, AES.MODE_CBC)
CTR_cipher = AES.new(key, AES.MODE_CTR)

ciphertext1 = CBC_cipher.encrypt(plaintext)
ciphertext2 = ECB_cipher.encrypt(plaintext)
ciphertext3 = CTR_cipher.encrypt(plaintext)

f = open("ciphertexts.txt", "w")

f.write(ciphertext1.hex() + '\n')
f.write(ciphertext2.hex() + '\n')
f.write(ciphertext3.hex())
f.close()
