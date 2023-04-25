from django.db import models

# Create your models here.

class Employee(models.Model):
    positions = [
        ('GD', 'Генеральный директор'),
        ('GB', 'Главный бухгалтер'),
        ('ID', 'Исполнительный директор'),
    ]
    employee_fullname = models.CharField('Фамилия Имя Отчество', max_length=200)
    employee_position = models.TextField('Должность', max_length=2,
        choices=positions,
        default='GD',
    )
    employee_birthdate = models.DateField('День рождения', null=True, blank=True)

    class Meta:
        verbose_name = ("Сотрудник")
        verbose_name_plural = ("Сотрудники")

    def __str__(self):
        return self.employee_fullname


    