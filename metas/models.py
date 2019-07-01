from django.db import models
from django.utils import timezone


class Post(models.Model):
    Autoria = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    Título_da_Meta = models.CharField(max_length=200)
    Descrição = models.TextField()
    Data_de_Criação  = models.DateTimeField(
            default=timezone.now)
    Prazo_de_Conclusão  = models.DateField()
    CONCLUIDA = 'CON'
    PARCIALMENTECONCLUIDA = 'PC'
    LONGEDESERCONCLUIDA = 'LC'
    NAOINICIADA = 'NI'
    Status_da_Meta = (
        (CONCLUIDA, 'Concluida com Sucesso'),
        (PARCIALMENTECONCLUIDA, 'Parcialmente Concluida'),
        (LONGEDESERCONCLUIDA, 'Longe de Ser Concluida'),
        (NAOINICIADA, 'Não Iniciada Ainda'),
    )
    status_meta = models.CharField(
        max_length=2,
        choices=Status_da_Meta,
        default=NAOINICIADA,)

    def is_upperclass(self):
        return self.status_meta in (self.LONGEDESERCONCLUIDA, self.NAOINICIADA)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
