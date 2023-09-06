from django.db import models
from django.core.validators import FileExtensionValidator
from datetime import datetime
from django.db import models
# Create your models here.
class uploads(models.Model):
    name=models.CharField(max_length=200)
    file = models.FileField(validators=[FileExtensionValidator(['pptx','docx','xlsx','pdf'])])
    date=models.DateTimeField(datetime.now().strftime("%d-%a-%Y"))
    
    

