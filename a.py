from Crypto.PublicKey import RSA
from Crypto import Random

secret_code = "taimurislam"


#-------generate public and private key----------#
key = RSA.generate(2048)

#-----------private key--------------------------#
private_key = key.exportKey(passphrase=secret_code, pkcs=8)
public_key  = key.publickey().exportKey()
public_key_1  = key.publickey()

print(private_key)
print(public_key)

private_file_out = open('private_key.bin', 'wb')
private_file_out.write(private_key)

public_file_out = open('public_key.bin', 'wb')
public_file_out.write(public_key)


