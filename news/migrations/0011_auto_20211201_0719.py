# Generated by Django 2.0 on 2021-12-01 04:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20211201_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='editor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Editor',
        ),
    ]
