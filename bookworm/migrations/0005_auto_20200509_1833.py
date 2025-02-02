# Generated by Django 3.0.5 on 2020-05-09 16:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookworm', '0004_authors_country_extra_user_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameModel(
            old_name='Authors',
            new_name='Author',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='bookworm.Author'),
        ),
        migrations.AlterField(
            model_name='author',
            name='country_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookworm.Country'),
        ),
        migrations.CreateModel(
            name='Prenotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('volume_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookworm.Volume')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('return_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('borrow_date', models.DateTimeField(default=datetime.datetime.now)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('volume_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookworm.Volume')),
            ],
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookworm.Country')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(to='bookworm.Genre'),
        ),
    ]
