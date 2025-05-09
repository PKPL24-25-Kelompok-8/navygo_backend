# Generated by Django 5.1.7 on 2025-04-01 10:52

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BillStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(auto_created=True, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('created_at', models.DateTimeField(auto_created=True, editable=False)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('payment_method', models.UUIDField()),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.billstatus')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('navygator_id', models.UUIDField()),
                ('service_id', models.UUIDField()),
                ('type', models.CharField(max_length=50)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='utils.bill')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=1000)),
                ('star_rating', models.DecimalField(decimal_places=0, max_digits=1)),
                ('bill', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='utils.bill')),
            ],
        ),
    ]
