# Generated by Django 4.2.4 on 2023-08-21 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frist_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=50)),
                ('instrument', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('release_date', models.DateField()),
                ('num_stars', models.IntegerField(choices=[(' ', '----select--'), ('1', 'Good'), ('2', 'Bad'), ('3', 'Not Good'), ('4', 'Excelent')])),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_app.musician')),
            ],
        ),
    ]
