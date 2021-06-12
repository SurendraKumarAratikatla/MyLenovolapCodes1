# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-06 18:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('is_primary', models.BooleanField(db_column='isPrimary')),
                ('address', models.CharField(max_length=512)),
                ('city', models.CharField(blank=True, db_index=True, max_length=48, null=True)),
                ('district', models.CharField(blank=True, max_length=48, null=True)),
                ('state', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('pin', models.CharField(blank=True, max_length=16, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('is_valid', models.BooleanField(db_column='isValid')),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('created_by', models.CharField(blank=True, db_column='createdBy', max_length=255, null=True)),
                ('updated_by', models.CharField(blank=True, db_column='updatedBy', max_length=255, null=True)),
            ],
            options={
                'db_table': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='Awardee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mid', models.CharField(max_length=36)),
                ('name', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=4)),
                ('description', models.CharField(blank=True, max_length=512, null=True)),
                ('specialization', models.CharField(blank=True, max_length=52, null=True)),
            ],
            options={
                'db_table': 'awardees',
            },
        ),
        migrations.CreateModel(
            name='LunarDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
            ],
            options={
                'db_table': 'lunarDates',
            },
        ),
        migrations.CreateModel(
            name='MaasamType',
            fields=[
                ('maasam', models.CharField(max_length=21, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'maasamTypes',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('mid', models.IntegerField(unique=True)),
                ('salutation', models.CharField(blank=True, max_length=63, null=True)),
                ('name', models.CharField(max_length=63)),
                ('surname', models.CharField(blank=True, max_length=63, null=True)),
                ('display_name', models.CharField(blank=True, db_column='displayName', max_length=15, null=True)),
                ('place', models.CharField(blank=True, max_length=63, null=True)),
                ('gender', models.CharField(blank=True, max_length=1, null=True)),
                ('birth_date', models.CharField(blank=True, db_column='birthDate', max_length=4, null=True)),
                ('birth_year', models.CharField(blank=True, db_column='birthYear', max_length=4, null=True)),
                ('email', models.CharField(blank=True, max_length=128, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('mobile', models.CharField(blank=True, max_length=24, null=True)),
                ('photo', models.CharField(blank=True, max_length=127, null=True)),
                ('search', models.CharField(blank=True, max_length=256, null=True)),
                ('gotram', models.CharField(blank=True, max_length=127, null=True)),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('created_by', models.CharField(blank=True, db_column='createdBy', max_length=255, null=True)),
                ('updated_by', models.CharField(blank=True, db_column='updatedBy', max_length=255, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'members',
            },
        ),
        migrations.CreateModel(
            name='NakshatramRasiPadamData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('created_by', models.CharField(blank=True, db_column='createdBy', max_length=255, null=True)),
                ('updated_by', models.CharField(blank=True, db_column='updatedBy', max_length=255, null=True)),
            ],
            options={
                'db_table': 'nakshatramRasiPadamData',
            },
        ),
        migrations.CreateModel(
            name='NakshatramType',
            fields=[
                ('nakshatram', models.CharField(max_length=63, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'nakshatramTypes',
            },
        ),
        migrations.CreateModel(
            name='OauthAccesstoken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=255, unique=True)),
                ('expires_at', models.IntegerField(blank=True, null=True)),
                ('scope', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'oauthAccessToken',
            },
        ),
        migrations.CreateModel(
            name='OauthAuthCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=255, unique=True)),
                ('redirect_uri', models.TextField()),
                ('expires_at', models.IntegerField(blank=True, null=True)),
                ('scope', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'oauthAuthCode',
            },
        ),
        migrations.CreateModel(
            name='OauthClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('random_id', models.CharField(max_length=255)),
                ('redirect_uris', models.TextField()),
                ('secret', models.CharField(max_length=255)),
                ('allowed_grant_types', models.TextField()),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'oauthClient',
            },
        ),
        migrations.CreateModel(
            name='OauthRefreshToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=255, unique=True)),
                ('expires_at', models.IntegerField(blank=True, null=True)),
                ('scope', models.CharField(blank=True, max_length=255, null=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.OauthClient')),
            ],
            options={
                'db_table': 'oauthRefreshTokens',
            },
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=127)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=63, null=True)),
                ('address', models.CharField(blank=True, max_length=511, null=True)),
                ('state', models.CharField(blank=True, max_length=127, null=True)),
                ('country', models.CharField(blank=True, max_length=63, null=True)),
                ('pincode', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('fax', models.CharField(blank=True, max_length=15, null=True)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
                ('parentid', models.CharField(blank=True, db_column='parentId', max_length=36, null=True)),
                ('owner', models.CharField(max_length=255)),
                ('status', models.BooleanField()),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('created_by', models.CharField(blank=True, db_column='createdBy', max_length=255, null=True)),
                ('updated_by', models.CharField(blank=True, db_column='updatedBy', max_length=255, null=True)),
                ('uri', models.CharField(blank=True, max_length=127, null=True)),
            ],
            options={
                'db_table': 'organisations',
            },
        ),
        migrations.CreateModel(
            name='PadamType',
            fields=[
                ('padam', models.CharField(max_length=1, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'padamTypes',
            },
        ),
        migrations.CreateModel(
            name='PakshamType',
            fields=[
                ('paksham', models.CharField(max_length=11, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'pakshamTypes',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('janmasamvatsara', models.CharField(blank=True, db_column='janmaSamvatsara', max_length=127, null=True)),
                ('timeofbirth', models.CharField(blank=True, db_column='timeOfBirth', max_length=127, null=True)),
                ('placeofbirth', models.CharField(blank=True, db_column='placeOfBirth', max_length=127, null=True)),
                ('countryofbirth', models.CharField(blank=True, db_column='countryOfBirth', max_length=35, null=True)),
                ('citizen', models.CharField(blank=True, max_length=35, null=True)),
                ('sutram', models.CharField(blank=True, max_length=127, null=True)),
                ('vaasara', models.CharField(blank=True, max_length=45, null=True)),
                ('religion', models.CharField(blank=True, max_length=48, null=True)),
                ('areasofinterest', models.CharField(blank=True, db_column='areasOfInterest', max_length=127, null=True)),
                ('associationsince', models.IntegerField(blank=True, db_column='associationSince', null=True)),
                ('community', models.CharField(blank=True, max_length=20, null=True)),
                ('subsect', models.CharField(blank=True, db_column='subSect', max_length=45, null=True)),
                ('mantropadesha', models.NullBooleanField()),
                ('kriyayoga', models.NullBooleanField(db_column='kriyaYoga')),
                ('sdhsmember', models.NullBooleanField(db_column='SDHSMember')),
                ('localashramassociation', models.IntegerField(blank=True, db_column='localAshramAssociation', null=True)),
                ('bloodgroup', models.CharField(blank=True, db_column='bloodGroup', max_length=5, null=True)),
                ('availablehrsperweek', models.IntegerField(blank=True, db_column='availableHrsPerWeek', null=True)),
                ('deathdate', models.CharField(blank=True, db_column='deathDate', max_length=45, null=True)),
                ('isprimary', models.NullBooleanField(db_column='isPrimary')),
                ('indianprofile', models.NullBooleanField(db_column='indianProfile')),
                ('profilestatus', models.CharField(blank=True, db_column='profileStatus', max_length=15, null=True)),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('created_by', models.CharField(blank=True, db_column='createdBy', max_length=255, null=True)),
                ('updated_by', models.CharField(blank=True, db_column='updatedBy', max_length=255, null=True)),
                ('janmamaasa', models.ForeignKey(blank=True, db_column='janmaMaasa', null=True, on_delete=django.db.models.deletion.CASCADE, to='member.MaasamType')),
                ('janmapaksha', models.ForeignKey(blank=True, db_column='janmaPaksha', null=True, on_delete=django.db.models.deletion.CASCADE, to='member.PakshamType')),
            ],
            options={
                'db_table': 'profiles',
            },
        ),
        migrations.CreateModel(
            name='RasiType',
            fields=[
                ('rasi', models.CharField(max_length=63, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'rasiTypes',
            },
        ),
        migrations.CreateModel(
            name='SequenceNumber',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
            ],
            options={
                'db_table': 'sequenceNumbers',
            },
        ),
        migrations.CreateModel(
            name='Seva',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('smid', models.CharField(blank=True, max_length=36, null=True)),
                ('ssid', models.CharField(max_length=36, unique=True)),
                ('sevadate', models.CharField(blank=True, db_column='sevaDate', max_length=63, null=True)),
                ('sevaday', models.CharField(blank=True, db_column='sevaDay', max_length=4, null=True)),
                ('islunar', models.CharField(blank=True, db_column='isLunar', max_length=4, null=True)),
                ('inthenameof', models.CharField(blank=True, db_column='inTheNameOf', max_length=127, null=True)),
                ('gotram', models.CharField(blank=True, max_length=127, null=True)),
                ('occasion', models.CharField(blank=True, max_length=40, null=True)),
                ('startdate', models.CharField(blank=True, db_column='startDate', max_length=10, null=True)),
                ('enddate', models.CharField(blank=True, db_column='endDate', max_length=10, null=True)),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('created_by', models.CharField(blank=True, db_column='createdBy', max_length=255, null=True)),
                ('updated_by', models.CharField(blank=True, db_column='updatedBy', max_length=255, null=True)),
                ('sevadatestd', models.DateField(blank=True, db_column='sevaDateStd', null=True)),
                ('mid', models.ForeignKey(db_column='mid', on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
                ('nakshatram', models.ForeignKey(blank=True, db_column='nakshatram', null=True, on_delete=django.db.models.deletion.CASCADE, to='member.NakshatramType')),
                ('oid', models.ForeignKey(db_column='oid', on_delete=django.db.models.deletion.CASCADE, to='member.Organisation')),
            ],
            options={
                'db_table': 'sevas',
            },
        ),
        migrations.CreateModel(
            name='SevaAddress',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=512)),
                ('city', models.CharField(blank=True, max_length=48, null=True)),
                ('district', models.CharField(blank=True, max_length=48, null=True)),
                ('state', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('pin', models.CharField(blank=True, max_length=16, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('isvalid', models.BooleanField(db_column='isValid')),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('created_by', models.CharField(blank=True, db_column='createdBy', max_length=255, null=True)),
                ('updated_by', models.CharField(blank=True, db_column='updatedBy', max_length=255, null=True)),
                ('sid', models.ForeignKey(db_column='sid', on_delete=django.db.models.deletion.CASCADE, to='member.Seva', unique=True)),
            ],
            options={
                'db_table': 'sevaAddresses',
            },
        ),
        migrations.CreateModel(
            name='SevaCategory',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=20, unique=True)),
                ('amount', models.IntegerField()),
                ('location', models.CharField(blank=True, max_length=63, null=True)),
                ('last_sequence_number', models.CharField(db_column='lastSequenceNumber', max_length=11)),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('created_by', models.CharField(blank=True, db_column='createdBy', max_length=255, null=True)),
                ('updated_by', models.CharField(blank=True, db_column='updatedBy', max_length=255, null=True)),
                ('status', models.BooleanField()),
                ('oid', models.ForeignKey(db_column='oid', on_delete=django.db.models.deletion.CASCADE, to='member.Organisation')),
            ],
            options={
                'db_table': 'sevaCategories',
            },
        ),
        migrations.CreateModel(
            name='SevasAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Address')),
                ('seva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Seva')),
            ],
            options={
                'db_table': 'seva_address',
            },
        ),
        migrations.CreateModel(
            name='SVExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
            ],
            options={
                'db_table': 'SVExtra',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.CharField(max_length=36)),
                ('tag', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='TithiType',
            fields=[
                ('tithi', models.CharField(max_length=15, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'tithiTypes',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transactiontype', models.CharField(db_column='transactionType', max_length=20)),
                ('transactionamount', models.CharField(db_column='transactionAmount', max_length=45)),
                ('checknumber', models.CharField(db_column='checkNumber', max_length=20)),
                ('cardtype', models.CharField(db_column='cardType', max_length=20)),
                ('cardnumber', models.CharField(db_column='cardNumber', max_length=45)),
                ('paymentdate', models.CharField(db_column='paymentDate', max_length=20)),
                ('paymentmethod', models.CharField(max_length=20)),
                ('creditcardtype', models.CharField(db_column='creditCardType', max_length=20)),
                ('lastfourdigits', models.CharField(db_column='lastFourDigits', max_length=4)),
                ('isdomestic', models.BooleanField(db_column='isDomestic')),
                ('transcurrencytype', models.CharField(db_column='transCurrencyType', max_length=20)),
                ('comments', models.CharField(max_length=255)),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('created_by', models.CharField(blank=True, db_column='createdBy', max_length=255, null=True)),
                ('updated_by', models.CharField(blank=True, db_column='updatedBy', max_length=255, null=True)),
                ('mid', models.ForeignKey(db_column='mid', on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
                ('oid', models.ForeignKey(db_column='oid', on_delete=django.db.models.deletion.CASCADE, to='member.Organisation')),
                ('scid', models.ForeignKey(db_column='scId', on_delete=django.db.models.deletion.CASCADE, to='member.SevaCategory')),
                ('sid', models.ForeignKey(db_column='sid', on_delete=django.db.models.deletion.CASCADE, to='member.Seva')),
            ],
            options={
                'db_table': 'transactions',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('username_canonical', models.CharField(max_length=255, unique=True)),
                ('email', models.CharField(max_length=255)),
                ('email_canonical', models.CharField(max_length=255, unique=True)),
                ('enabled', models.BooleanField()),
                ('salt', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('locked', models.BooleanField()),
                ('expired', models.BooleanField()),
                ('expires_at', models.DateTimeField(blank=True, null=True)),
                ('confirmation_token', models.CharField(blank=True, max_length=255, null=True)),
                ('password_requested_at', models.DateTimeField(blank=True, null=True)),
                ('roles', models.TextField()),
                ('credentials_expired', models.BooleanField()),
                ('credentials_expire_at', models.DateTimeField(blank=True, null=True)),
                ('mid', models.CharField(blank=True, max_length=36, null=True)),
                ('googleid', models.CharField(blank=True, db_column='googleId', max_length=255, null=True, unique=True)),
                ('googleaccesstoken', models.CharField(blank=True, db_column='googleAccessToken', max_length=255, null=True)),
                ('facebookid', models.CharField(blank=True, db_column='facebookId', max_length=255, null=True, unique=True)),
                ('facebookaccesstoken', models.CharField(blank=True, db_column='facebookAccessToken', max_length=255, null=True)),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.AddField(
            model_name='seva',
            name='sid',
            field=models.ForeignKey(db_column='sid', on_delete=django.db.models.deletion.CASCADE, to='member.SevaCategory'),
        ),
        migrations.AddField(
            model_name='profile',
            name='janmatithi',
            field=models.ForeignKey(blank=True, db_column='janmaTithi', null=True, on_delete=django.db.models.deletion.CASCADE, to='member.TithiType'),
        ),
        migrations.AddField(
            model_name='profile',
            name='mid',
            field=models.ForeignKey(db_column='mid', on_delete=django.db.models.deletion.CASCADE, to='member.Member', unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='padam',
            field=models.ForeignKey(blank=True, db_column='padam', null=True, on_delete=django.db.models.deletion.CASCADE, to='member.PadamType'),
        ),
        migrations.AddField(
            model_name='oauthrefreshtoken',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.User'),
        ),
        migrations.AddField(
            model_name='oauthauthcode',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.OauthClient'),
        ),
        migrations.AddField(
            model_name='oauthauthcode',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.User'),
        ),
        migrations.AddField(
            model_name='oauthaccesstoken',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.OauthClient'),
        ),
        migrations.AddField(
            model_name='oauthaccesstoken',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.User'),
        ),
        migrations.AddField(
            model_name='nakshatramrasipadamdata',
            name='nakshatram',
            field=models.ForeignKey(db_column='nakshatram', on_delete=django.db.models.deletion.CASCADE, to='member.NakshatramType'),
        ),
        migrations.AddField(
            model_name='nakshatramrasipadamdata',
            name='padam',
            field=models.ForeignKey(db_column='padam', on_delete=django.db.models.deletion.CASCADE, to='member.PadamType'),
        ),
        migrations.AddField(
            model_name='nakshatramrasipadamdata',
            name='rasi',
            field=models.ForeignKey(db_column='rasi', on_delete=django.db.models.deletion.CASCADE, to='member.RasiType'),
        ),
        migrations.AddField(
            model_name='member',
            name='nakshatram',
            field=models.ForeignKey(blank=True, db_column='nakshatram', null=True, on_delete=django.db.models.deletion.CASCADE, to='member.NakshatramType'),
        ),
        migrations.AddField(
            model_name='lunardate',
            name='maasam',
            field=models.ForeignKey(db_column='maasam', on_delete=django.db.models.deletion.CASCADE, to='member.MaasamType'),
        ),
        migrations.AddField(
            model_name='lunardate',
            name='paksham',
            field=models.ForeignKey(blank=True, db_column='paksham', null=True, on_delete=django.db.models.deletion.CASCADE, to='member.PakshamType'),
        ),
        migrations.AddField(
            model_name='lunardate',
            name='tithi',
            field=models.ForeignKey(db_column='tithi', on_delete=django.db.models.deletion.CASCADE, to='member.TithiType'),
        ),
        migrations.AddField(
            model_name='awardee',
            name='member',
            field=models.ForeignKey(db_column='member', on_delete=django.db.models.deletion.CASCADE, to='member.Member'),
        ),
        migrations.AddField(
            model_name='address',
            name='mid',
            field=models.ForeignKey(db_column='mid', on_delete=django.db.models.deletion.CASCADE, to='member.Member'),
        ),
        migrations.AlterUniqueTogether(
            name='sevasaddress',
            unique_together=set([('seva', 'address')]),
        ),
        migrations.CreateModel(
            name='DonationAsset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_column='created', default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(db_column='updated', default=django.utils.timezone.now, editable=False)),
                ('ocassionName', models.CharField(blank=True, max_length=45, null=True)),
                ('ocassionDate', models.DateField(blank=True, null=True)),
                ('assetType', models.CharField(blank=True, choices=[('land', 'Land'), ('building', 'Building'), ('equipment', 'Equipment')], default='equipment', max_length=20, null=True)),
                ('dateOfDonation', models.DateField(blank=True, null=True)),
                ('value', models.IntegerField(blank=True, null=True)),
                ('subType', models.CharField(blank=True, max_length=20, null=True)),
                ('assetLocation', models.CharField(blank=True, max_length=150, null=True)),
                ('dateOfRegistration', models.DateField(blank=True, null=True)),
                ('extent', models.CharField(blank=True, max_length=20, null=True)),
                ('notes', models.TextField()),
                ('created_by', models.ForeignKey(blank=True, db_column='createdBy', editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='donationasset_created_by', to=settings.AUTH_USER_MODEL)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
                ('organisation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.Organisation')),
                ('updated_by', models.ForeignKey(blank=True, db_column='updatedBy', editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='donationasset_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DonationCash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_column='created', default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(db_column='updated', default=django.utils.timezone.now, editable=False)),
                ('ocassionName', models.CharField(blank=True, max_length=45, null=True)),
                ('ocassionDate', models.DateField(blank=True, null=True)),
                ('receiptNo', models.CharField(blank=True, max_length=15, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('instruementDetails', models.CharField(blank=True, max_length=45, null=True)),
                ('dateOfDonation', models.DateField(blank=True, null=True)),
                ('notes', models.TextField()),
                ('created_by', models.ForeignKey(blank=True, db_column='createdBy', editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='donationcash_created_by', to=settings.AUTH_USER_MODEL)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
                ('organisation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.Organisation')),
                ('updated_by', models.ForeignKey(blank=True, db_column='updatedBy', editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='donationcash_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DonationKind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_column='created', default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(db_column='updated', default=django.utils.timezone.now, editable=False)),
                ('ocassionName', models.CharField(blank=True, max_length=45, null=True)),
                ('ocassionDate', models.DateField(blank=True, null=True)),
                ('material', models.CharField(blank=True, max_length=45, null=True)),
                ('quantity', models.FloatField(blank=True, null=True)),
                ('units', models.CharField(blank=True, max_length=5, null=True)),
                ('value', models.IntegerField(blank=True, null=True)),
                ('certifiedBy', models.CharField(blank=True, max_length=30, null=True)),
                ('dateOfDonation', models.DateField(blank=True, null=True)),
                ('notes', models.TextField()),
                ('created_by', models.ForeignKey(blank=True, db_column='createdBy', editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='donationkind_created_by', to=settings.AUTH_USER_MODEL)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
                ('organisation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.Organisation')),
                ('updated_by', models.ForeignKey(blank=True, db_column='updatedBy', editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='donationkind_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DonationService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_column='created', default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(db_column='updated', default=django.utils.timezone.now, editable=False)),
                ('capacity', models.CharField(max_length=30)),
                ('fromDate', models.DateField(blank=True, null=True)),
                ('toDate', models.DateField(blank=True, null=True)),
                ('ocassionName', models.CharField(blank=True, max_length=45, null=True)),
                ('created_by', models.ForeignKey(blank=True, db_column='createdBy', editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='donationservice_created_by', to=settings.AUTH_USER_MODEL)),
                ('organisation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.Organisation')),
                ('updated_by', models.ForeignKey(blank=True, db_column='updatedBy', editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='donationservice_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
