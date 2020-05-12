from django.contrib import admin

from .models import Question, Choice
# from .models import Choice

# admin.site.register(Question)
#admin.site.register(Choice)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    search_fields = ['question_text']
    fieldsets = [
        (None,               {'fields':['question_text']}),
        ('Date information', {'fields':['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
admin.site.register(Question,QuestionAdmin)
