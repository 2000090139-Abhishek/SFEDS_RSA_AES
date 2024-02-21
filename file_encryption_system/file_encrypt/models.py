from django.db import models

# Create your models here.
class EncryptedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    encrypted_file = models.FileField(upload_to='encrypted/')
    public_key = models.TextField()
    private_key = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
