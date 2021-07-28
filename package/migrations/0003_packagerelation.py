# Generated by Django 3.2.5 on 2021-07-28 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('box', '0003_alter_box_name'),
        ('product', '0001_initial'),
        ('package', '0002_auto_20210728_0824'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackageRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boxes', to='box.box')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='package', to='package.package')),
                ('product', models.ManyToManyField(null=True, related_name='products', to='product.Product')),
            ],
        ),
    ]
