# Generated by Django 3.2.6 on 2022-03-18 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0003_alter_subject_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='level2_subjects',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='level2_subject_set', to='subjects.subject', verbose_name='二级学科'),
        ),
        migrations.AddField(
            model_name='subject',
            name='level3_subjects',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='level3_subject_set', to='subjects.subject', verbose_name='三级学科'),
        ),
    ]
