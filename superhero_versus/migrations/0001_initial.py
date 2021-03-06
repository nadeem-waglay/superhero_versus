# Generated by Django 3.2.12 on 2022-03-28 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Superhero',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('full_name', models.CharField(max_length=255)),
                ('intelligence', models.IntegerField()),
                ('strength', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('durability', models.IntegerField()),
                ('power', models.IntegerField()),
                ('combat', models.IntegerField()),
            ],
        ),
    ]
