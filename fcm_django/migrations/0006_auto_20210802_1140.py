# Generated by Django 3.1.12 on 2021-08-02 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fcm_django", "0005_auto_20170808_1145"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fcmdevice",
            name="device_id",
            field=models.CharField(
                blank=True,
                db_index=True,
                help_text="Unique device identifier",
                max_length=3072,
                null=True,
                verbose_name="Device ID",
            ),
        ),
    ]
