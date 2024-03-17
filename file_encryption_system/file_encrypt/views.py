from django.shortcuts import render, redirect
from .models import EncryptedFile
from .forms import FileForm
from .utils import encrypt_file, decrypt_file
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import EncryptedFile
# from .forms import UploadFileForm

# from Crypto.PublicKey import RSA

# def generate_keypair():
#     key = RSA.generate(2048)
#     private_key = key.export_key()
#     public_key = key.publickey().export_key()
#     return private_key, public_key
# public_key = "-----BEGIN PUBLIC KEY-----\n2000090139\n-----END PUBLIC KEY-----"

# def upload_file(request):
#     if request.method == 'POST':
#         form = FileForm(request.POST, request.FILES)
#         if form.is_valid():
#             # Ensure that the public_key argument is passed to the encrypt_file function
#             encrypted_file_path = encrypt_file(form.cleaned_data['file'], public_key)

#             # Save the encrypted file path to the database
#             encrypted_file = EncryptedFile.objects.create(encrypted_file=encrypted_file_path)

#             return redirect('file_encrypt:file_list')
#     else:
#         form = FileForm()

#     return render(request, 'file_encrypt/upload_file.html', {'form': form})

from django.shortcuts import render
from .utils import generate_keys, load_keys, encrypt_file, decrypt_file

# def upload_file(request):
#     if request.method == 'POST':
#         # Generate keys (you may want to save these keys securely for later use)
#         public_key, private_key = generate_keys()

#         # Get the uploaded file
#         uploaded_file = request.FILES['file']

#         # Encrypt file content
#         encrypted_content = encrypt_file(uploaded_file.read(), public_key)

#         # Save the encrypted content or perform other actions

#     return render(request, 'upload_file.html')
def upload_file(request):
    if request.method == 'POST':
        # Generate keys (you may want to save these keys securely for later use)
        public_key, private_key = generate_keys()

        # Get the uploaded file
        uploaded_file = request.FILES['file']

        # Encrypt file content
        encrypted_content = encrypt_file(uploaded_file.read(), public_key)

        # Save the encrypted content or perform other actions

    return render(request, 'upload_file.html')

def file_list(request):
    files = EncryptedFile.objects.all()
    return render(request, 'file_encrypt/file_list.html', {'files': files})

# private_key= """-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAsO7GJi9veXeT7v1cUR+PJviHVH9hWUEw4nYorVTOIgXGYjXhTyfTK8wrKmfOnYKzoR/wIaftr3lOrnlLm0PxTUD/WNH47vm6qyvVOY8pPs163rtZwEgacAmpZ1yO7oLPj0vI/knUuDz4F4giUb7i7wN5nQZ8p7wan62SbMr7l76LA4/bPuHqxv8s0iFbCSWOL0LBIKDXtmzksCBrbw4TKZnbvDW762JGIRpctqFapVVS4R8u
# eh74/afEU8MJkF2SgpmkxGLNE+uRLnzw5ynrnrk927w3A8mihaDbcsvOctMiUjXP
# eUMUyNBU6jL9nk114TI/UZnn7aXSXOFetc215wIDAQABAoIBAARtHMDky+Weg7Fl
# XjNbVkHz0rLe8ukANABeU1sutW9tdI6NaYMI7IP6ehP3/9e55tN/kIrPACe1Ia5E
# s4sBUp6LozeuHQuhbLWOhamIdtAu5MWAq1iflSW7YCUJUDwQQrADhdYys6MeR1iT
# W8RuwY+YJykx+dlaX9IhzflxxISBwZRBRM1opXT9ERQMtHQ/zs+RIXvjUZjj6A7o
# tmhawCnI/VsJ9+CUTAiE06+1i9a8gH0fqAPc2KBccP6aQgM7TGpAi/TE9YstWa4p
# zWtHVNKZ4QJ8GlDrGMsF73iPgH0pWNzERgR6t3nGrCgEdUfKrPt8CpktrQdTYwic
# qlorZKUCgYEAv3RsyFQDdqST3pT7Ps+bHFVybe/7vve9rCqsyFjTuvWTP9jsZSXw
# j4Oa04dEhmwqwxvT83oGudpKm5+2naiyB0xpzp7qptWFlp14hyBjMf21KUikg4Q6
# 6azkkJmUz0RUjtzp64eX0NTmtoG9taf9HAf7Nj9WDZ0btvX4RL7xKH0CgYEA7JUE
# JfB/idFMTOS5+qkkyOvbjzmTdF6Tl1SJNrYshd6/JopPrQi3LixQlQvhn3rtoT1E
# zo35aN/mCvNnb6dyIzYJZGxfWfwNn3QiEWK558fJWjySEm5lJ4jo32vW4bkFU1fD
# iANa25Ikfv5C9LKhvOXH7NpSf4QUoTf1NVDDSTMCgYAqaWonvqS9xZuUNUCrG2Zr
# Emq0+/KyzULRPurjvvm4cupZvH4xsgPmZusHbPG7LX8TlbiQOToANeFNNEZKCrLV
# dxIBWab1qltbkCrBFGWlD2Twbk0zbTl3xnsjpUIX4DUzKLERIgp5kpBBYeBau4oQ
# iZwW2lT/0wvurfJ/mCToKQKBgQDBW21fgLcMMZZVxh7GYhWhbTsuTNVaJ64i4cGf
# iLbM1ueNnT9PYa8tOqTFnEdT68lpncStuNWeRFgknRjt5YHgi1qTzAsGZX3Q077A
# TNs6N0w2xwhvrfBYpooFiILAS1Kx8inp8SwCBuhzLmYUziZoV7jVuP3yIEYoGa78
# WzywhwKBgD/aWFX4bcqRUg/dT7EoindzeK6xKHqU/hbetoWSkWh/cbe6YTHgMY65
# h1okZMes1mRUMpMmDqv+RNW+qo06R1i2B+8BBgIvq8Pv+gSNQVx/hSbcgfdTB231
# 7LcxRcS9YoFN2c1HWzvUBv0Xc1OHIcD1xNPeXKsNhx1p/hrgPRYB\n
# -----END RSA PRIVATE KEY-----"""

# def decrypt_file_view(request, file_id):
#     encrypted_file_instance = get_object_or_404(EncryptedFile, pk=file_id)
#     if not encrypted_file_instance.encrypted_file or not encrypted_file_instance.file_encrypt.path:
#         return HttpResponse("File not found.", status=404)
#     try:
#         decrypted_file_path = decrypt_file(encrypted_file_instance.encrypted_file.path, private_key)
#     except Exception as e:
#         return HttpResponse(f"Error decrypting file: {e}", status=500)

#     # Return the decrypted file as a response
#     with open(decrypted_file_path, 'rb') as decrypted_file:
#         response = HttpResponse(decrypted_file.read(), content_type='application/octet-stream')
#         response['Content-Disposition'] = f'attachment; filename="{encrypted_file_instance.encrypted_file.name}"'
#         return response

# def get_encrypted_content_by_id(file_id):
#     file_instance = get_object_or_404(EncryptedFile, id=file_id)
#     return file_instance.encrypted_content_field 

# def decrypt_file_view(request, file_id):
#     # Load keys (retrieve these keys securely from storage)
#     public_key, private_key = load_keys(public_key_data, private_key_data)

#     # Retrieve encrypted file content from the database
#     encrypted_file = get_object_or_404(FileForm, file_id=file_id)
#     encrypted_content = encrypted_file.encrypted_content

#     # Decrypt file content
#     decrypted_content = decrypt_file(encrypted_content, private_key)

#     # Render the decrypted content or perform other actions

#     return render(request, 'decrypted_file.html', {'decrypted_content': decrypted_content})
def decrypt_file_view(request, file_id):
    # Generate keys (you may want to load these keys securely from storage)
    public_key, private_key = generate_keys()

    # Retrieve encrypted file content from the database
    encrypted_file = get_object_or_404(EncryptedFile, file_id=file_id)
    encrypted_content = encrypted_file.encrypted_content

    # Decrypt file content
    decrypted_content = decrypt_file(encrypted_content, private_key)

    # Render the decrypted content or perform other actions

    return render(request, 'decrypted_file.html', {'decrypted_content': decrypted_content})