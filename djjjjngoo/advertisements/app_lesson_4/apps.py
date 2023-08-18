from django.apps import AppConfig
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone

class AppLesson4Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_lesson_4'
    verbose_name = 'Объявления'


@admin.display(description='дата обновления')
def create_dat_e(self):
    if self.updated_at.date() == timezone.now().date():
        created_time = self.updated_at.time().strftime('%H:$M:%S')
        return format_html(
            '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
        )
    return self.updated_at.strftime('%d.%m.%Y')
