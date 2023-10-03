# Generated by Django 3.1.7 on 2023-07-19 02:58

from django.db import migrations, models


def set_default_value(apps, schema_editor):
    DataFileUpload = apps.get_model('homeApp', 'DataFileUpload')
    DataFileUpload.objects.update(actual_file='path/to/default_file')
    
class Migration(migrations.Migration):

    initial = True

    dependencies = [
        
    ]


    operations = [
        migrations.CreateModel(
            name='DataFileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=50)),
                ('actual_file', models.FileField(upload_to='uploads/')),
                ('description', models.CharField(max_length=400)),
            ],
        ),
        migrations.RunPython(set_default_value),  # Chama a função para definir o valor padrão
    ]
