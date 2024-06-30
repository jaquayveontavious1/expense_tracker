# Generated by Django 5.0.6 on 2024-06-30 19:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('category', models.CharField(choices=[('groceries', 'Groceries'), ('transport', 'Transport'), ('entertainment', 'Entertainment'), ('loans', 'Loans'), ('food', 'Food'), ('insurance', 'Insurance'), ('travel', 'Travel'), ('rent', 'Rent')], max_length=100)),
                ('description', models.TextField(max_length=255)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]