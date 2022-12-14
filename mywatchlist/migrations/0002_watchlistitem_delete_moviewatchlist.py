# Generated by Django 4.1 on 2022-09-21 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mywatchlist", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="WatchlistItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("watched", models.BooleanField()),
                ("title", models.CharField(max_length=50)),
                ("rating", models.IntegerField()),
                ("release_date", models.TextField()),
                ("review", models.TextField()),
            ],
        ),
        migrations.DeleteModel(name="movieWatchlist",),
    ]
