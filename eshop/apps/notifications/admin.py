from django.contrib import admin

from .models import Notification



admin.site.register(Notification)

# Register your models here.

'''class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0
    

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    date_hierarchy = 'pub_date'
    search_fields = ['question_text']
    inlines = [ChoiceInline]
    
admin.site.register(Question, QuestionAdmin)

class ChoiceAdmin(admin.ModelAdmin):
    raw_id_fields = ['question']
    
admin.site.register(Choice, ChoiceAdmin)
'''
