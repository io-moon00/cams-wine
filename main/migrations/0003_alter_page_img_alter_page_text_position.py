# Generated by Django 4.2.7 on 2023-12-31 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_page_main_page_page_text_position_alter_page_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='page',
            name='text_position',
            field=models.CharField(choices=[('center', 'Center'), ('left', 'Left'), ('right', 'Right')], default='center', max_length=6),
        ),
    ]
