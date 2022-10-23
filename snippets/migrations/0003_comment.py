# Generated by Django 4.1 on 2022-10-23 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snippets', '0002_rename_update_at_snippet_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='本文')),
                ('commented_at', models.DateTimeField(auto_now_add=True, verbose_name='投稿日')),
                ('commented_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='投稿者')),
                ('commented_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snippets.snippet', verbose_name='スニペット')),
            ],
        ),
    ]