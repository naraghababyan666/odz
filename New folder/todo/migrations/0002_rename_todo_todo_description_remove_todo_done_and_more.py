# Generated by Django 4.1 on 2022-08-23 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='todo',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='done',
        ),
        migrations.AddField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('Todo', 'Todo'), ('Done', 'Done')], default='Todo', max_length=255),
        ),
    ]
