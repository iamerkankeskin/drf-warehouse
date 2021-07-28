# Generated by Django 3.2.5 on 2021-07-27 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Cardboard Name')),
                ('volume', models.IntegerField(verbose_name='Volume')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('product', models.ManyToManyField(null=True, related_name='box_product', to='product.Product')),
            ],
        ),
    ]
