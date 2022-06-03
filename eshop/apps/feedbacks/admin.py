from django.contrib import admin

from apps.feedbacks.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'user', 'user_phone', 'feedback', 'is_published', 'created_on', ]
    search_fields = ['user_phone', 'feedback', ]
    save_on_top = True


admin.site.register(Feedback, FeedbackAdmin)
