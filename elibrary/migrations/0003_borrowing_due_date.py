# Generated by Django 5.1.7 on 2025-03-08 18:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("elibrary", "0002_remove_borrowing_due_date_borrowing_return_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="borrowing",
            name="due_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
