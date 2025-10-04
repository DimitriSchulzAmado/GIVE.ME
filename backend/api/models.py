import uuid
from django.db import models
from django.contrib.auth.models import User

#Classe para criar uma tablea nesse caso itens
class Item(models.Model):

    STATUS_CHOICES = [('new', 'Novo'), ('used', 'Usado')]
    LISTING_STATE_CHOICES = [('active', 'Ativo'), ('inactive', 'Inativo')]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    title = models.TextField()
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='items')
    city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=False)
    listing_state = models.CharField(max_length=20, choices=LISTING_STATE_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self): return self.title

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(unique=True, null=False)
    slug = models.TextField(unique=True, null=False)
    def __str__(self): return self.name

class ItemPhoto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='photos')
    url = models.TextField()
    position = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(null=False)
    state = models.TextField(null=True, blank=True)
    def __str__(self): return self.name


class UserProfile(models.Model):
    # Ligação 1 para 1 com o User. Se o user for deletado, o perfil também é.
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True) 
    # Campo para armazenar a URL da foto (ou usar ImageField para upload de arquivo)
    photo_url = models.TextField(null=True, blank=True) 
    def __str__(self): return f"Profile for {self.user.username}"    