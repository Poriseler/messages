# Generated by Django 3.2.3 on 2021-05-22 19:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Messege',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=160)),
                ('created', models.DateTimeField(auto_now=True)),
                ('last_update', models.DateTimeField()),
                ('views', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', related_query_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
