# Generated by Django 4.2.1 on 2023-06-07 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_category_remove_article_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(default='not-categorized', max_length=100),
        ),
    ]
