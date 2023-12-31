# Generated by Django 4.2.7 on 2023-12-31 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='main_page',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='page',
            name='text_position',
            field=models.CharField(choices=[('center', 'center'), ('left', 'Left'), ('right', 'Right')], default='center', max_length=6),
        ),
        migrations.AlterField(
            model_name='page',
            name='img',
            field=models.ImageField(default=1, upload_to='uploads'),
            preserve_default=False,
        ),
    ]
