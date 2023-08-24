from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=50)
    instrument=models.CharField(max_length=40)

    def __str__(self):
        return self.first_name + " "+ self.last_name
    class Meta:
         db_table="Musician"
        
    

class Album(models.Model):
    artist=models.ForeignKey(Musician, on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    release_date=models.DateField()
    rating=(
    
    ( 1,'Good'),
    (2,'Bad'),
    (3,'Not Good'),
    (4,'Excelent',)
    
    )
    num_stars=models.IntegerField(choices=rating)
    class Meta:
        db_table="Album"

    def __str__(self):
        return self.name + " Rating: "+ str( self.num_stars)
