# Generated by Django 2.1.5 on 2019-08-14 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rainforest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('reviews', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rainforest.Product')),
            ],
        ),
    ]
