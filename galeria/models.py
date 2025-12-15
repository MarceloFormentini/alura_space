from datetime import datetime
from django.db import models

class Fotografia(models.Model):

    OPCAOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("PLANETA", "Planeta"),
        ("GALAXIA", "Galáxia"),
        ("COMETA", "Cometa"),
        ("ASTEROIDE", "Asteroide"),
        ("CINTURA_DE_ASTEROIDES", "Cintura de Asteroides"),
        ('OUTROS', 'Outros'),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCAOES_CATEGORIA, default='OUTROS')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f"Fotografia: [nome: {self.nome}]"