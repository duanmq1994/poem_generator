from django.contrib import admin
from .models import WordType, Words, Rules

class WordsInline(admin.TabularInline):
    model = Words
    extra = 1 # 默认提供一个选项填写位

class WordTypeAdmin(admin.ModelAdmin):
    inlines = [WordsInline]
    search_fields = ['type_name']

# Register your models here.
admin.site.register(WordType, WordTypeAdmin)
admin.site.register(Rules)