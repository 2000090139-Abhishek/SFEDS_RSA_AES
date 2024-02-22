# file_encrypt/utils.py
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

def generate_keypair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def encrypt_file(file_path, public_key):
    # Load the public key
    recipient_key = RSA.import_key(public_key)

    # Generate a random session key for AES encryption
    session_key = AES.new(b'sixteen byte key', AES.MODE_EAX).nonce

    # Use the RSA public key to encrypt the session key
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    # Use the session key to encrypt the file with AES
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    with open(file_path, 'rb') as file:
        plaintext = file.read()
        ciphertext, tag = cipher_aes.encrypt_and_digest(plaintext)

    # Save the encrypted file and other necessary information
    with open(file_path + '.enc', 'wb') as encrypted_file:
        for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext):
            encrypted_file.write(x)

    return file_path + '.enc'


def decrypt_file(encrypted_file_path, private_key):
    # Load the private key
    recipient_key = RSA.import_key(private_key)

    # Read the encrypted file and extract the necessary information
    with open(encrypted_file_path, 'rb') as encrypted_file:
        enc_session_key, nonce, tag, ciphertext = \
            [encrypted_file.read(x) for x in (recipient_key.size_in_bytes(), 16, 16, -1)]

    # Use the RSA private key to decrypt the session key
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    session_key = cipher_rsa.decrypt(enc_session_key)

    # Use the session key to decrypt the file with AES
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher_aes.decrypt_and_verify(ciphertext, tag)

    # Save the decrypted content to a new file
    decrypted_file_path = encrypted_file_path[:-4]  # Remove the '.enc' extension
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(plaintext)

    return decrypted_file_path
    