from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

recipient_public_key = RSA.import_key(open("public_key.bin").read())
session_key = get_random_bytes(16)

print(session_key)
print(recipient_public_key)
print(recipient_public_key.publickey())
print(recipient_public_key.publickey().exportKey())

encrypted_data_file_out = open("encrypted_data.bin", "wb")

#----------------encrypt the session key with the public RSA KEY-------------------#
cipher_rsa = PKCS1_OAEP.new(recipient_public_key)
encrypt_session_key = cipher_rsa.encrypt(session_key)
encrypted_data_file_out.write(cipher_rsa.encrypt(session_key))

#----------------encrypt data with AES Session key-----------------#
data = "taimurislamjoy".encode('utf-8')
print(data)
cipher_aes = AES.new(session_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(data)
[ encrypted_data_file_out.write(x) for x in (cipher_aes.nonce, tag, ciphertext) ]