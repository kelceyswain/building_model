# Generated by Django 3.0.3 on 2020-02-06 09:56

from django.db import migrations, models
import payload.models


class Migration(migrations.Migration):

    dependencies = [
        ('payload', '0002_auto_20200206_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='body',
            field=models.ImageField(upload_to='uploads/', validators=[payload.models.Image.validate_image]),
        ),
    ]