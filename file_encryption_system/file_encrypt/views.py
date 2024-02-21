from django.shortcuts import render, redirect
from .models import EncryptedFile
from .forms import FileForm
from .utils import encrypt_file, decrypt_file

def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save()
            public_key, private_key = encrypt_file(file_instance.file.path)
            file_instance.public_key = public_key
            file_instance.private_key = private_key
            file_instance.save()
            return redirect('file_encrypt:file_list')
    else:
        form = FileForm()
    return render(request, 'file_encrypt/upload_file.html', {'form': form})

def file_list(request):
    files = EncryptedFile.objects.all()
    return render(request, 'file_encrypt/file_list.html', {'files': files})

def decrypt_file_view(request, file_id):
    encrypted_file = EncryptedFile.objects.get(pk=file_id)
    decrypted_path = decrypt_file(encrypted_file.encrypted_file.path, encrypted_file.private_key)
    return render(request, 'file_encrypt/decrypted_file.html', {'decrypted_path': decrypted_path})
