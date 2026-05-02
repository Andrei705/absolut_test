from django.db import models


class BaseModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AuthorRole(models.Model):
    """Роль пользователя"""
    name_role = models.CharField(max_length=150, help_text='Название роли')


class Author(BaseModel):
    """Пользователь"""
    full_name = models.CharField(max_length=255, help_text='Полное имя')
    email = models.CharField(max_length=255, help_text='email')
    user_role = models.ForeignKey(AuthorRole, related_name='author_authorrole',  null=True, on_delete=models.DO_NOTHING, blank=True)


class Survey(BaseModel):
    """Опрос"""
    survey_name = models.TextField(help_text='Название опроса')
    author = models.ForeignKey(Author, related_name='survey_author', null=True, on_delete=models.DO_NOTHING, blank=True)


class Question(BaseModel):
    """Вопросы"""
    question = models.TextField(help_text='Вопрос')
    sorted = models.PositiveIntegerField(default=0)


class AnswerToQuestion(BaseModel):
    """Ответы на вопросы"""
    answer = models.TextField(help_text='Ответ')
    survey = models.ForeignKey(Survey, related_name='answertoquestion_survey', null=True, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Question, related_name='answertoquestion_question', null=True, on_delete=models.DO_NOTHING)
    sorted = models.PositiveIntegerField(default=0)


class UserResponse(BaseModel):
    """Ответ пользователя"""
    answer = models.BooleanField(default=False, help_text='Ответ')
    author = models.ForeignKey(Author, related_name='userresponse_author', null=True, on_delete=models.DO_NOTHING, blank=True)
    answer_to_question = models.ForeignKey(AnswerToQuestion, related_name='userresponse_answertoquestion', null=True, on_delete=models.DO_NOTHING)




