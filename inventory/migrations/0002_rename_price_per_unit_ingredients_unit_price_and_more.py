# Generated by Django 4.2.19 on 2025-02-23 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredients',
            old_name='price_per_unit',
            new_name='unit_price',
        ),
        migrations.RenameField(
            model_name='menuitems',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='menuitems',
            name='recipe',
        ),
        migrations.AddField(
            model_name='menuitems',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('date', models.DateField()),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.ingredients')),
            ],
        ),
    ]
