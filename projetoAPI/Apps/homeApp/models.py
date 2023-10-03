from django.db import models

# Create your models here.
#class DataFileUpload(models.Model):
#    file_name = models.CharField(max_length=50)
#    actual_file = models.FileField(upload_to ='uploads/')
#    description = models.CharField(max_length=400,null=True,blank=True)
    
#    def __str__(self):
#        return self.file_name
#class DataFileUpload(models.Model):
    # Atributos do modelo, se houver

    # Atributos para armazenar temporariamente os dados do arquivo
#    file_name = models.CharField(max_length=255, null=True, blank=True)
#    file_content = models.TextField(null=True, blank=True)
#    cpf_name = models.CharField(max_length=255, null=True, blank=True)


class DataFileUpload(models.Model):
    file_name = models.CharField(max_length=255)
    actual_file = models.FileField(upload_to='uploads/')  # Campo para armazenar o arquivo
    description = models.TextField()
    file_content = models.TextField(null=True, blank=True)
    cpf_name = models.CharField(max_length=255, null=True, blank=True)

    # Outros campos e métodos do modelo (se houver)

    def __str__(self):
        return self.file_name
