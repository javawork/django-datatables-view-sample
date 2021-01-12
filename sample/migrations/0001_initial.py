# Generated by Django 2.1.3 on 2018-12-05 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('pos', models.CharField(max_length=8)),
                ('age', models.CharField(max_length=8)),
                ('tm', models.CharField(max_length=8)),
                ('g', models.CharField(max_length=8)),
                ('gs', models.CharField(max_length=8)),
                ('mp', models.CharField(max_length=8)),
                ('fg', models.CharField(max_length=8)),
                ('fga', models.CharField(max_length=8)),
                ('fgp', models.CharField(max_length=8)),
                ('threep', models.CharField(max_length=8)),
                ('threepa', models.CharField(max_length=8)),
                ('threepp', models.CharField(max_length=8)),
                ('twop', models.CharField(max_length=8)),
                ('twopa', models.CharField(max_length=8)),
                ('twopp', models.CharField(max_length=8)),
                ('efgp', models.CharField(max_length=8)),
                ('ft', models.CharField(max_length=8)),
                ('fta', models.CharField(max_length=8)),
                ('ftp', models.CharField(max_length=8)),
                ('orb', models.CharField(max_length=8)),
                ('drb', models.CharField(max_length=8)),
                ('trb', models.CharField(max_length=8)),
                ('ast', models.CharField(max_length=8)),
                ('stl', models.CharField(max_length=8)),
                ('blk', models.CharField(max_length=8)),
                ('tov', models.CharField(max_length=8)),
                ('pf', models.CharField(max_length=8)),
                ('pts', models.CharField(max_length=8)),
            ],
            options={
                'verbose_name': 'nba',
                'verbose_name_plural': 'nba',
            },
        ),
    ]
