# Generated by Django 2.1.9 on 2019-09-21 02:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20190920_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='rsvp time'),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name="rsvp'd by"),
        ),
    ]