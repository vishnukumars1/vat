# Generated by Django 5.0.4 on 2024-07-02 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0002_remove_creditnotereference_credit_note_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='openingbalance',
            field=models.DecimalField(blank=True, decimal_places=2, default='0', max_digits=10, null=True),
        ),
    ]
