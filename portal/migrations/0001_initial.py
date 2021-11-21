# Generated by Django 3.2.9 on 2021-11-21 13:27

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
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.ManyToManyField(to='portal.Country')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_config', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]