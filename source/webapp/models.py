from django.db import models



STATUS_CHOICES = [
    ('active', 'Активно'),
    ('blocked', 'Заблокировано')
]


class Card(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Имя')
    mail = models.EmailField(max_length=200, null=False, blank=False, verbose_name='Почта')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='active', verbose_name='Статус')

    def __str__(self):
        return "{}. {}".format(self.pk, self.name)

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'
