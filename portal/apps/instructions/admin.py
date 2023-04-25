from django.contrib import admin

# Register your models here.

from .models import Instruction

# admin.site.register(Instruction)

class InstructionAdmin(admin.ModelAdmin):
    readonly_fields = ('instruction_date',)

admin.site.register(Instruction, InstructionAdmin)
