# Generated by Django 4.2.7 on 2023-11-05 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0004_alter_ticket_status'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='upvote',
            unique_together={('user', 'ticket')},
        ),
        migrations.AddField(
            model_name='upvote',
            name='session_key',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='upvote',
            name='vote_weight',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='upvote',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='upvote',
            unique_together={('session_key', 'ticket'), ('user', 'ticket')},
        ),
        migrations.AlterIndexTogether(
            name='upvote',
            index_together={('session_key', 'ticket'), ('user', 'ticket')},
        ),
    ]
