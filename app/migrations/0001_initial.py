# Generated by Django 5.0.4 on 2024-07-11 14:16

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=16, validators=[django.core.validators.MinLengthValidator(16), django.core.validators.MaxLengthValidator(16)], verbose_name='Номер счета')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=100, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Баланс')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to=settings.AUTH_USER_MODEL, verbose_name='Владелец счета')),
            ],
            options={
                'verbose_name': 'Счет',
                'verbose_name_plural': 'Счета',
            },
        ),
    ]
