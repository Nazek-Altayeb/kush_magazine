# Generated by Django 4.2.1 on 2023-06-24 18:01

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("article", "0008_delete_category_remove_article_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="body",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
