from django.db import models

# Create your models here.

class BaseModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AuthorRole(models.Model):
    """Роль пользователя"""
    name_role = models.CharField(max_length=150, help_text='Название роли')
    # TODO: задаем роли по задумке:
    #  Admin(superuser) может все изменять, удалять, создавать, редактировать
    #  User может читать и проходить тест


class Author(BaseModel):
    """Пользователь"""
    full_name = models.CharField(max_length=255, help_text='Полное имя')
    email = models.CharField(max_length=255, help_text='email')
    user_role = models.ForeignKey(AuthorRole, related_name='author_authorrole',  null=True, on_delete=models.DO_NOTHING, blank=True)


class Survey(BaseModel):
    """Опрос"""
    survey_name = models.TextField(help_text='Название опроса')
    author = models.ForeignKey(AuthorRole, related_name='survey_authorrole', null=True, on_delete=models.DO_NOTHING, blank=True)
    #TODO: так же можно использовать поля models.JSONField, ArrayField правда тогда с сортировкой не вяжется


class Question(BaseModel):
    """Варианты ответов"""
    question = models.TextField(help_text='Вопрос')
    answer = models.TextField(help_text='Ответ')
    survey = models.ForeignKey(Survey, related_name='question_survey', null=True, on_delete=models.DO_NOTHING)
    sorted = models.PositiveIntegerField()
    # TODO: по задумке поле sorted можно менять , тем самым изменять сортировку как нужно пользователю
