# from django.db import models

# # Create your models here.
# # class EncryptedFile(models.Model):
# #     file = models.FileField(upload_to='uploads/')
# #     encrypted_file = models.FileField(upload_to='encrypted_file/')
# #     public_key = models.TextField()
# #     private_key = models.TextField()
# #     created_at = models.DateTimeField(auto_now_add=True)
# class EncryptedFile(models.Model):
#     file_id = models.AutoField(primary_key=True)
#     encrypted_content = models.BinaryField()

#     # def __str__(self):
#     #     return self.file.name
    
from django.db import models

class EncryptedFile(models.Model):
    file_id = models.AutoField(primary_key=True)
    encrypted_content = models.BinaryField(default=b'')
    public_key = models.TextField()
    private_key = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"EncryptedFile {self.file_id}"


