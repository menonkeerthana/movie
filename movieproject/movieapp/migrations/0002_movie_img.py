# Generated by Django 4.2.6 on 2023-10-12 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movieapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="img",
            field=models.ImageField(default=1, upload_to="gallery"),
            preserve_default=False,
        ),
    ]
