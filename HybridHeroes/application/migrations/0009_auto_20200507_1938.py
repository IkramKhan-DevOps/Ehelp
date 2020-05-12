# Generated by Django 3.0.2 on 2020-05-07 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0008_auto_20200506_2109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='category',
            new_name='request_category',
        ),
        migrations.RenameField(
            model_name='request',
            old_name='support',
            new_name='supply',
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='facebook',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='instagram',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
