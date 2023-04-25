from django.db import models

# Create your models here.

class Question(models.Model):
    themes = [
        ('FI', 'Финансы'),
        ('RT', 'Продажи'),
        ('MK', 'Маркетинг')
    ]
    question_main = models.CharField('Формулировка вопроса', max_length=200)
    question_answer = models.TextField('Ответ', max_length=200)
    question_theme = models.TextField('Тема', max_length=2,
        choices=themes,
        default='FI',
    )

    class Meta:
        verbose_name = ("Вопрос")
        verbose_name_plural = ("Вопросы")

    def __str__(self):
        return self.question_main
    