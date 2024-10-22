# Generated by Django 3.0.5 on 2020-05-26 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookworm', '0010_auto_20200526_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='country_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookworm.Country'),
        ),
        migrations.AlterField(
            model_name='book',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bookworm.Country'),
        ),
        migrations.AlterField(
            model_name='editor',
            name='country_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookworm.Country'),
        ),
    ]
