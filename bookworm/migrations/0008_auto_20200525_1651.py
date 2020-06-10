# Generated by Django 3.0.5 on 2020-05-25 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookworm', '0007_auto_20200525_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='country_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookworm.Country'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookworm.Language'),
        ),
        migrations.AlterField(
            model_name='editor',
            name='country_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookworm.Country'),
        ),
    ]
