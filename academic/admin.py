from django.contrib import admin
from .models import Question, Answer, Comment

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']
admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['subject']
admin.site.register(Answer, AnswerAdmin)

class CommentAdmin(admin.ModelAdmin):
    search_fields = ['subject']
admin.site.register(Comment, CommentAdmin)
