# Generated by Django 3.2.9 on 2022-03-20 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments_app', '0001_initial'),
        ('publication_app', '0010_merge_0009_auto_20220316_1016_0009_post_user'),
        ('likes_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='comments_app.comment'),
        ),
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='publication_app.post'),
        ),
    ]
