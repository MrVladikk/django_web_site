# Generated by Django 5.1.1 on 2024-09-20 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_remove_post_llikes_post_likes_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
