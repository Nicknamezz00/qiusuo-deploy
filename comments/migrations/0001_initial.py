# Generated by Django 3.2.6 on 2022-03-31 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.BigIntegerField(verbose_name='帖子id')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('content', models.TextField(verbose_name='内容')),
                ('approved', models.BigIntegerField(default=0, verbose_name='赞成')),
                ('category', models.CharField(max_length=20, null=True, verbose_name='种类')),
            ],
        ),
    ]
