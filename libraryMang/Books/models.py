from django.db import models

# Create your models here.
CATEGORY = (
    ("Fiction", "Fiction"), ("Non-Ficton", "Non-Ficton"), ("History", "History"), ("Geography", "Geography"), ("Science", "Science"), ("Horror", "Horror"), ("Biographies", "Biographies")
)

LANGUAGE = (
    ("English", "English"), ("Hindi", "Hindi"), ("Marathi", "Marathi"), ("Gujarati", "Gujarati"), ("Other", "Other")
)

class Books(models.Model):
    
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    category = models.CharField(choices=CATEGORY,max_length=30)
    synopsis = models.CharField(max_length=300)
    isbn = models.CharField(max_length=12)
    pages = models.IntegerField()
    language = models.CharField(choices=LANGUAGE,max_length=12)
    

    def __str__(self):
        return self.title
    