from Crypto.PublicKey import RSA
from Crypto import Random

secret_code = "taimurislam"

private_key = open('private_key.bin', 'rb').read()

key_pair = RSA.import_key(private_key, passphrase=secret_code)

public_key = key_pair.publickey().exportKey()

print(public_key)