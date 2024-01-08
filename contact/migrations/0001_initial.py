# Generated by Django 3.2.23 on 2024-01-08 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=254, null=True)),
                ('text', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('message', models.TextField(max_length=500)),
                ('order_number', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('topic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contact.topic')),
            ],
        ),
    ]
