# Generated by Django 5.0.2 on 2024-02-23 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_encrypt', '0004_remove_encryptedfile_encrypted_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encryptedfile',
            name='encrypted_content',
            field=models.BinaryField(),
        ),
    ]