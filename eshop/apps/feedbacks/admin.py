from django.contrib import admin

from apps.feedbacks.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'feedback_to', 'user_name', 'user_email', 'user_phone', 'feedback', 'is_published', 'is_deleted',
                    'created_at',
                    'updated_at']
    search_fields = ['user_email', 'user_phone', 'feedback', ]
    save_on_top = True


admin.site.register(Feedback, FeedbackAdmin)
