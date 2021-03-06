from django.db import models

from eventex.subscriptions import cpffield


class Subscription(models.Model):
    name = models.CharField('nome', max_length=100)
    cpf = cpffield.CPFField('CPF', max_length=14)
    email = models.EmailField('e-mail', blank=True)
    phone = models.CharField('telefone', max_length=20, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    paid = models.BooleanField('pago', default=False)

    class Meta:
        verbose_name = 'inscrição'
        verbose_name_plural = 'inscrições'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

