# Generated by Django 3.2.6 on 2022-03-05 10:04

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='年龄')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('qq', models.CharField(blank=True, max_length=20, null=True, verbose_name='QQ号码')),
                ('avatar', models.URLField(default='avatar/default.png')),
                ('phone', models.CharField(blank=True, default=None, max_length=11, null=True, verbose_name='手机号码')),
                ('gender', models.IntegerField(choices=[(1, '男'), (2, '女'), (3, '未知')], null=True, verbose_name='性别')),
                ('intro', models.CharField(blank=True, default='你还没有写上个人介绍哦', max_length=300, null=True, verbose_name='个人介绍')),
                ('post_count', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['id'],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_str', models.TextField(verbose_name='用户头衔')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='title_set', to='users.userinfo', verbose_name='头衔拥有者')),
            ],
        ),
    ]
