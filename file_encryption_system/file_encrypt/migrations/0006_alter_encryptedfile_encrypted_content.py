# Generated by Django 5.0.2 on 2024-02-23 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_encrypt', '0005_alter_encryptedfile_encrypted_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encryptedfile',
            name='encrypted_content',
            field=models.BinaryField(default=b''),
        ),
    ]
