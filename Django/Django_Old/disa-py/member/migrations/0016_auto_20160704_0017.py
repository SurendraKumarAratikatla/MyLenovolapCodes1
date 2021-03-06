# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-03 18:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0015_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_column='created', default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(db_column='updated', default=django.utils.timezone.now, editable=False)),
                ('status', models.CharField(choices=[('self', 'Self'), ('working', 'Working'), ('department', 'Department'), ('retired', 'Retired')], max_length=65)),
                ('fbid', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(choices=[(b'm', b'Male'), (b'f', b'Female'), (b'd', b'Data Not Available')], default='D', max_length=1)),
                ('duty', models.CharField(blank=True, max_length=255, null=True)),
                ('department', models.CharField(blank=True, max_length=255, null=True)),
                ('knowssriswamijisince', models.IntegerField(blank=True, null=True)),
                ('martialstatus', models.CharField(choices=[(b'single', b'Single'), (b'married', b'Married')], default='single', max_length=7)),
                ('residentspouse', models.BooleanField(default=True)),
                ('dateofjoining', models.DateField(blank=True, null=True)),
                ('dateofregistration', models.DateTimeField(blank=True, null=True)),
                ('note', models.CharField(blank=True, max_length=255, null=True)),
                ('headofthefamily', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'staffProfile',
            },
        ),
        migrations.RenameField(
            model_name='assetequipment',
            old_name='contarctorname',
            new_name='contractorname',
        ),
        migrations.RemoveField(
            model_name='assetbuilding',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='assetbuilding',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='assetequipment',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='assetequipment',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='assetequipment',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='assetequipment',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='assetland',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='assetland',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='complimentary',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='complimentary',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='honorary',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='honorary',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='medicalprofile',
            name=b'created_by',
        ),
        migrations.RemoveField(
            model_name='medicalprofile',
            name=b'updated_by',
        ),
        migrations.RemoveField(
            model_name='member',
            name=b'facebookId',
        ),
        migrations.RemoveField(
            model_name='member',
            name=b'googleId',
        ),
        migrations.RemoveField(
            model_name='member',
            name=b'twitterId',
        ),
        migrations.RemoveField(
            model_name='trustee',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='trustee',
            name='updated_by',
        ),
        migrations.AddField(
            model_name='member',
            name='facebookid',
            field=models.CharField(blank=True, db_column='facebookId', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='googleid',
            field=models.CharField(blank=True, db_column='googleId', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='twitterid',
            field=models.CharField(blank=True, db_column='twitterId', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='assetbuilding',
            name='contractoraddress',
            field=models.TextField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='assetbuilding',
            name='currentstate',
            field=models.CharField(choices=[(b'excellent', b'Excellent'), (b'good', b'Good'), (b'poor', b'Poor'), (b'urgentrepair', b'UrgentRepair'), (b'abandon', b'Abandon')], default='excellent', max_length=15),
        ),
        migrations.AlterField(
            model_name='assetbuilding',
            name='maindonors',
            field=models.ForeignKey(db_column='maindonors', on_delete=django.db.models.deletion.CASCADE, related_name='maindonors', to='member.Member'),
        ),
        migrations.AlterField(
            model_name='assetbuilding',
            name='organisation',
            field=models.ForeignKey(db_column='organisation', on_delete=django.db.models.deletion.CASCADE, related_name='organisation', to='member.Organisation'),
        ),
        migrations.AlterField(
            model_name='assetequipment',
            name='currentstate',
            field=models.CharField(choices=[(b'excellent', b'Excellent'), (b'good', b'Good'), (b'poor', b'Poor'), (b'urgentrepair', b'UrgentRepair'), (b'abandon', b'Abandon')], default='excellent', max_length=15),
        ),
        migrations.AlterField(
            model_name='assetequipment',
            name='government_permission_required',
            field=models.BooleanField(default='No'),
        ),
        migrations.AlterField(
            model_name='assetland',
            name='enclosure',
            field=models.CharField(blank=True, help_text='(Please provide comma separated list of Enclosed Document Number & Names)', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='assetland',
            name='inchargeperson',
            field=models.ForeignKey(db_column='inchargeperson', on_delete=django.db.models.deletion.CASCADE, related_name='inchargeperson', to='member.Member'),
        ),
        migrations.AlterField(
            model_name='assetland',
            name='land_type',
            field=models.CharField(choices=[(b'gift', b'Gift'), (b'sale', b'Sale'), (b'lease', b'Lease'), (b'will', b'Will'), (b'exchange', b'Exchange'), (b'license', b'Licenses'), (b'allotment', b'Allotment')], max_length=15),
        ),
        migrations.AlterField(
            model_name='assetland',
            name='regn_fees',
            field=models.IntegerField(blank=True, help_text='(in Rs)', null=True),
        ),
        migrations.AlterField(
            model_name='assetland',
            name='total',
            field=models.IntegerField(blank=True, help_text='(Total in Rs)', null=True),
        ),
        migrations.AlterField(
            model_name='assetland',
            name='value',
            field=models.IntegerField(blank=True, help_text='(Value in Rs)', null=True),
        ),
        migrations.AlterField(
            model_name='honorary',
            name='member',
            field=models.ForeignKey(db_column='member', on_delete=django.db.models.deletion.CASCADE, related_name='Honoraryemember', to='member.Member'),
        ),
        migrations.AlterField(
            model_name='medicalprofile',
            name='aec',
            field=models.CharField(blank=True, help_text='cells/c.mm', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='medicalprofile',
            name='consultingDoctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultingDoctor', to='member.Member'),
        ),
        migrations.AlterField(
            model_name='medicalprofile',
            name='dce',
            field=models.CharField(blank=True, help_text='DC:E-', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='medicalprofile',
            name='dcl',
            field=models.CharField(blank=True, help_text='DC:L-', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='medicalprofile',
            name='dcm',
            field=models.CharField(blank=True, help_text='DC:M-', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='medicalprofile',
            name='dcn',
            field=models.CharField(blank=True, help_text='DC:N-', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='medicalprofile',
            name='esr',
            field=models.CharField(blank=True, help_text='mm/hr', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='medicalprofile',
            name='hb',
            field=models.CharField(blank=True, help_text='gm%', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='medicalprofile',
            name='height',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='medicalprofile',
            name='mid',
            field=models.ForeignKey(db_column='mid', on_delete=django.db.models.deletion.CASCADE, related_name='member', to='member.Member', unique=True),
        ),
        migrations.AlterField(
            model_name='medicalprofile',
            name='scholestrol',
            field=models.CharField(blank=True, help_text='s.cholestrol (mg%)', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='medicalprofile',
            name='shdl',
            field=models.CharField(blank=True, help_text='s.hdl (mg%)', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='medicalprofile',
            name='sldl',
            field=models.CharField(blank=True, help_text='s,ldl (mg%)', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='medicalprofile',
            name='striglycerides',
            field=models.CharField(blank=True, help_text='mg%', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='medicalprofile',
            name='svldlmg',
            field=models.CharField(blank=True, help_text='s.vldl (mg%)', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='medicalprofile',
            name='tc',
            field=models.CharField(blank=True, help_text='cells/c.mm', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='medicalprofile',
            name='weight',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='trustee',
            name='active',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=15),
        ),
        migrations.AlterField(
            model_name='trustee',
            name='member',
            field=models.ForeignKey(db_column='member', on_delete=django.db.models.deletion.CASCADE, related_name='trusteemember', to='member.Member'),
        ),
        migrations.AlterField(
            model_name='trustee',
            name='tenure_active',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'No')], max_length=15),
        ),
        migrations.AlterField(
            model_name='trustee',
            name='valid',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='yes', max_length=15),
        ),
        migrations.AddField(
            model_name='staffprofile',
            name='children',
            field=models.ForeignKey(blank=True, db_column='children', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='member.Member'),
        ),
        migrations.AddField(
            model_name='staffprofile',
            name='contacts',
            field=models.ForeignKey(blank=True, db_column='contacts', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='member.Member'),
        ),
        migrations.AddField(
            model_name='staffprofile',
            name='father',
            field=models.ForeignKey(blank=True, db_column='father', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='father', to='member.Member'),
        ),
        migrations.AddField(
            model_name='staffprofile',
            name='introducer',
            field=models.ForeignKey(blank=True, db_column='introducer', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='introducer', to='member.Member'),
        ),
        migrations.AddField(
            model_name='staffprofile',
            name='mid',
            field=models.ForeignKey(db_column='mid', on_delete=django.db.models.deletion.CASCADE, related_name='memberstaff', to='member.Member'),
        ),
        migrations.AddField(
            model_name='staffprofile',
            name='mother',
            field=models.ForeignKey(blank=True, db_column='mother', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mother', to='member.Member'),
        ),
        migrations.AddField(
            model_name='staffprofile',
            name='spousename',
            field=models.ForeignKey(db_column='spousename', on_delete=django.db.models.deletion.CASCADE, related_name='spousename', to='member.Member'),
        ),
    ]
