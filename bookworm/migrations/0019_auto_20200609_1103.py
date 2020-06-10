# Generated by Django 3.0.5 on 2020-06-09 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookworm', '0018_auto_20200609_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='extra_user_info',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='author',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookworm.Country'),
        ),
        migrations.AlterField(
            model_name='editor',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookworm.Country'),
        ),
    ]