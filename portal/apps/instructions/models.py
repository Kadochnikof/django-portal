from django.db import models
# from portal.apps.employees.models import Employee

# Create your models here.

class Instruction(models.Model):
    instruction_name = models.CharField('Тема', max_length=200)
    instruction_author = models.ForeignKey('employees.Employee', on_delete=models.DO_NOTHING, null=True, verbose_name='Автор') # Автор (это поле связано с моделью Employee)
    instruction_date = models.DateTimeField('Дата создания', auto_now_add=True)
    instruction_url = models.URLField('Ссылка на инструкцию', max_length = 200)

    class Meta:
        verbose_name = ("Инструкция")
        verbose_name_plural = ("Инструкции")

    def __str__(self):
        return self.instruction_name


    