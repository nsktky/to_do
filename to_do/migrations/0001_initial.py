# Generated by Django 3.1.5 on 2021-01-18 05:16
# makemigrationsすると作成されるファイル makemigrationsする際はアプリ名指定するほうがベター

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoModel',
            fields=[
                # model作成時にidが自動生成される DetailViewで使用するpkはidを用いる
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('memo', models.TextField()),
            ],
        ),
    ]
