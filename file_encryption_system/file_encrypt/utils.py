# # file_encrypt/utils.py
# from Crypto.PublicKey import RSA
# from Crypto.Cipher import AES, PKCS1_OAEP

# def generate_keypair():
#     key = RSA.generate(2048)
#     private_key = key.export_key()
#     public_key = key.publickey().export_key()
#     return private_key, public_key

# def encrypt_file(file_path, public_key):
#     recipient_key = RSA.import_key(public_key)
#     session_key = AES.new(b'sixteen byte key', AES.MODE_EAX).nonce
#     cipher_rsa = PKCS1_OAEP.new(recipient_key)
#     enc_session_key = cipher_rsa.encrypt(session_key)
#     cipher_aes = AES.new(session_key, AES.MODE_EAX)
#     with open(file_path, 'rb') as file:
#         plaintext = file.read()
#         ciphertext, tag = cipher_aes.encrypt_and_digest(plaintext)
#     with open(file_path + '.enc', 'wb') as encrypted_file:
#         for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext):
#             encrypted_file.write(x)
#     return file_path + '.enc'


# def decrypt_file(encrypted_file_path, private_key):
#     recipient_key = RSA.import_key(private_key)
#     with open(encrypted_file_path, 'rb') as encrypted_file:
#         enc_session_key, nonce, tag, ciphertext = \
#             [encrypted_file.read(x) for x in (recipient_key.size_in_bytes(), 16, 16, -1)]
#     cipher_rsa = PKCS1_OAEP.new(recipient_key)
#     session_key = cipher_rsa.decrypt(enc_session_key)
#     cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce=nonce)
#     plaintext = cipher_aes.decrypt_and_verify(ciphertext, tag)
#     decrypted_file_path = encrypted_file_path[:-4] 
#     with open(decrypted_file_path, 'wb') as decrypted_file:
#         decrypted_file.write(plaintext)

#     return decrypted_file_path
    
from Crypto.PublicKey import RSA

def generate_keys():
    key = RSA.generate(2048)  # Adjust the key size based on your requirements
    public_key = key.publickey().export_key()
    private_key = key.export_key()

    return public_key, private_key

def load_keys(public_key_path, private_key_path):
    public_key_data = open(public_key_path, 'rb').read()
    private_key_data = open(private_key_path, 'rb').read()

    public_key = RSA.import_key(public_key_data)
    private_key = RSA.import_key(private_key_data)

    return public_key, private_key

from Crypto.Cipher import PKCS1_OAEP

def encrypt_file(plaintext, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def decrypt_file(ciphertext, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_text = cipher.decrypt(ciphertext)
    return decrypted_text