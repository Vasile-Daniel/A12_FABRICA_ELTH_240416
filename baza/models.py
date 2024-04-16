from django.db import models

# Create your models here.
class Material(models.Model):
    nume = models.CharField(max_length=100, null=True, blank=True)
    cantitate = models.IntegerField(default=0)
    descriere = models.TextField(blank=True)

    def __str__(self):
        return self.nume 


class Comanda(models.Model):
    nume_client = models.CharField(max_length=100, blank=True, null=True)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    cantitate = models.IntegerField(default=0)
    data_plasare = models.DateField(auto_now_add= True)

    def __str__(self):
        return f"{self.nume_client} - {self.material.nume}"


class RaportCalitate(models.Model):
     material = models.OneToOneField(Material, on_delete=models.CASCADE)
     test_rezultat = models.CharField(max_length=100, blank= True, null=True)
     data_test = models.DateField(auto_now_add=True)


     def __str__(self):
         return f"Raport pentru {self.material.nume}" 
    