# Generated by Django 3.0.3 on 2020-02-13 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payload', '0005_auto_20200213_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='building',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='payload.Building'),
        ),
        migrations.AddField(
            model_name='sound',
            name='building',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='payload.Building'),
        ),
        migrations.AddField(
            model_name='text',
            name='building',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='payload.Building'),
        ),
        migrations.AddField(
            model_name='video',
            name='building',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='payload.Building'),
        ),
    ]
