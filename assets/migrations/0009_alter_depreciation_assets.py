# Generated by Django 4.0.2 on 2022-02-04 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0008_alter_assets_current_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depreciation',
            name='assets',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='depreciation', to='assets.assets'),
        ),
    ]
