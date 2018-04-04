from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP


secret_code = "taimurislam"
private_key_file = open("private_key.bin", 'rb').read()
print(private_key_file)


private_key = RSA.import_key(private_key_file, passphrase=secret_code)
print(private_key)


file_in = open("encrypted_data.bin", "rb")
enc_session_key, nonce, tag, ciphertext = [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]

cipher_rsa = PKCS1_OAEP.new(private_key)
session_key = cipher_rsa.decrypt(enc_session_key)
print(session_key)

cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
data = cipher_aes.decrypt_and_verify(ciphertext, tag)
print(data)