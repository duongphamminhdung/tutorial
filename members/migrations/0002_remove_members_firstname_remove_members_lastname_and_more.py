# Generated by Django 4.1.7 on 2023-04-21 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="members", name="firstname",),
        migrations.RemoveField(model_name="members", name="lastname",),
        migrations.AddField(
            model_name="members",
            name="content",
            field=models.TextField(default=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="members",
            name="title",
            field=models.CharField(default=9, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="members",
            name="tomtat",
            field=models.CharField(default=9, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="members",
            name="type",
            field=models.CharField(default=9, max_length=225),
            preserve_default=False,
        ),
    ]
