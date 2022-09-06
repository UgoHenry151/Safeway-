# Generated by Django 4.0.4 on 2022-07-07 11:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pharmacy', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordr_no', models.CharField(max_length=50)),
                ('things_bought', models.CharField(blank=True, max_length=500, null=True)),
                ('itm_paid', models.BooleanField(default=False)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('total', models.FloatField()),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('firstname', models.CharField(blank=True, max_length=200, null=True)),
                ('pharmacy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pharmacy.pharmacy')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Paidorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('cart_no', models.CharField(blank=True, max_length=36, null=True)),
                ('payment_code', models.CharField(max_length=50)),
                ('paid_item', models.BooleanField(default=False)),
                ('firstname', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Paidorder',
                'verbose_name_plural': 'Paidorders',
                'db_table': 'paidorder',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Drugscart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product_name', models.CharField(max_length=100)),
                ('total', models.IntegerField(default=1)),
                ('order_no', models.CharField(max_length=50)),
                ('item_paid', models.BooleanField(default=False)),
                ('pharmacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.pharmacy')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Drugscart',
                'verbose_name_plural': 'Drugscarts',
                'db_table': 'drugscart',
                'managed': True,
            },
        ),
    ]
