# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SponsorItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, db_column='created')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, db_column='updated')),
                ('code', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=523)),
                ('amount', models.FloatField()),
                ('photo', models.CharField(max_length=255, null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='sponsoritem_created_by', db_column='createdBy', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'db_table': 'sponsorItems',
            },
        ),
        migrations.AddField(
            model_name='seva',
            name='title',
            field=models.CharField(max_length=55, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='sevacategory',
            name='duration',
            field=models.CharField(max_length=11, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='sevacategory',
            name='duration_type',
            field=models.CharField(max_length=11, null=True, db_column='durationType', blank=True),
        ),
        migrations.AddField(
            model_name='sevacategory',
            name='recurrence',
            field=models.CharField(max_length=25, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='sevacategory',
            name='show_start_date',
            field=models.BooleanField(default=True, db_column='showStartDate'),
        ),
        migrations.AddField(
            model_name='sevacategory',
            name='sponsor_item_type',
            field=models.CharField(max_length=55, null=True, db_column='sponsorItemType', blank=True),
        ),
        migrations.AlterField(
            model_name='seva',
            name='enddate',
            field=models.DateField(null=True, db_column='endDate', blank=True),
        ),
        migrations.AlterField(
            model_name='seva',
            name='startdate',
            field=models.DateField(null=True, db_column='startDate', blank=True),
        ),
        migrations.AddField(
            model_name='sponsoritem',
            name='seva_id',
            field=models.ForeignKey(db_column='sevaId', to='member.Seva', unique=True),
        ),
        migrations.AddField(
            model_name='sponsoritem',
            name='updated_by',
            field=models.ForeignKey(related_name='sponsoritem_updated_by', db_column='updatedBy', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
