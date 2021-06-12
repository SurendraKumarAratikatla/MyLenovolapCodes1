from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings
import member.models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0009_importGroup'),

    ]

    operations = [
        migrations.CreateModel(
            name='MedicalProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                #('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                #('member', models.ForeignKey(db_column='member', to='member.Member', blank=False, unique=True)),
                ('mid', models.ForeignKey(db_column='mid', unique=True, on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
		('height', models.IntegerField(blank=True)),
	        ('weight', models.IntegerField(blank=True)),
                ('diabetes', models.CharField(max_length=255, blank=True, null=True)),
                ('hypertension', models.CharField(max_length=255, blank=True, null=True)),
                ('tuberculosis', models.CharField(max_length=255, blank=True, null=True)),
                ('musculoskeletalproblems', models.CharField(max_length=255, blank=True, null=True)),
		('gastrointestinalproblem', models.CharField(max_length=255, blank=True, null=True)),
                ('renalproblrms', models.CharField(max_length=255, blank=True, null=True)),
                ('cardiacdiseases', models.CharField(max_length=255, blank=True, null=True)),
                ('chestdiseases', models.CharField(max_length=255, blank=True, null=True)),
                ('nervoussystemdisorders', models.CharField(max_length=255, blank=True, null=True)),
                ('anymajororminorsurgeriesinpast', models.CharField(max_length=255, blank=True, null=True)),
                ('menstrualproblemsandobstetricalhistory', models.CharField(max_length=255, blank=True, null=True)),
                ('familyhistory', models.CharField(max_length=255, blank=True, null=True)),
                ('pulse', models.CharField(max_length=255, blank=True, null=True)),
                ('bp', models.CharField(max_length=255, blank=True, null=True)),
                ('rr', models.CharField(max_length=255, blank=True, null=True)),
                ('temp', models.CharField(max_length=255, blank=True, null=True)),
                ('pallor', models.CharField(max_length=255, blank=True, null=True)),
                ('icterus', models.CharField(max_length=255, blank=True, null=True)),
                ('edema',  models.CharField(max_length=255, blank=True, null=True)),
                ('lnpathy',  models.CharField(max_length=255, blank=True, null=True)),
                ('cyanosis', models.CharField(max_length=255, blank=True, null=True)),
                ('clubbing', models.CharField(max_length=255, blank=True, null=True)),
                ('skin', models.CharField(max_length=255, blank=True, null=True)),
                ('hair', models.CharField(max_length=255, blank=True, null=True)),
                ('oralcavityteeth', models.CharField(max_length=255, blank=True, null=True)),
                ('eye', models.CharField(max_length=255, blank=True, null=True)),
                ('ent', models.CharField(max_length=255, blank=True, null=True)),
                ('skeletalsystem', models.CharField(max_length=255, blank=True, null=True)),
                ('cns', models.CharField(max_length=255, blank=True, null=True)),
                ('cvs', models.CharField(max_length=255, blank=True, null=True)),
                ('chest', models.CharField(max_length=255, blank=True, null=True)),
                ('abdomen', models.CharField(max_length=255, blank=True, null=True)),
                ('genitals', models.CharField(max_length=255, blank=True, null=True)),
                ('hb', models.CharField( max_length=255, blank=True, null=True)),
                ('tc', models.CharField(max_length=255, blank=True, null=True)),
                ('dcn', models.CharField(max_length=255, blank=True, null=True)),
                ('dcl', models.CharField(max_length=255, blank=True, null=True)),
                ('dce', models.CharField(max_length=255, blank=True, null=True)),
                ('dcm', models.CharField(max_length=255, blank=True, null=True)),
                ('esr', models.CharField(max_length=255, blank=True, null=True)),
                ('aec', models.CharField(max_length=255, blank=True, null=True)),
                ('lipidprofile', models.CharField(max_length=255, blank=True, null=True)),
                ('vdrl', models.CharField(max_length=255, blank=True, null=True)),
                ('striglycerides', models.CharField(max_length=255, blank=True, null=True)),
                ('urineanalysis', models.CharField(max_length=255, blank=True, null=True)),
                ('scholestrol', models.CharField(max_length=255, blank=True, null=True)),
                ('shdl', models.CharField( max_length=255, blank=True, null=True)),
                ('sldl', models.CharField( max_length=255, blank=True, null=True)),
                ('svldlmg', models.CharField(max_length=255, blank=True, null=True)),
                ('thyroidprofile', models.CharField(max_length=255, blank=True, null=True)),
                ('xray', models.CharField(max_length=255, blank=True, null=True)),
                ('usg', models.CharField(max_length=255, blank=True, null=True)),
                ('impressioninsummary', models.CharField(max_length=255, blank=True, null=True)),
                ('consultingDoctor', models.ForeignKey(db_column='consultingDoctor', on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
                ('indian', models.BooleanField(default=True)),
                ('dnd_mails',models.BooleanField(default=True)),
                ('dnd_sms',  models.BooleanField(default=True)),
                ('dnd_emails', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, db_column='created')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, db_column='updated')),
                ('created_by', models.ForeignKey(related_name='medicalProfie_created_by', db_column='createdBy', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('updated_by', models.ForeignKey(related_name='medicalProfile_updated_by', db_column='updatedBy', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),

            ],
            options={
                'db_table': 'medicalProfile',
            },
       ),
       migrations.AddField(
            model_name='Member',
            name='googleId',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),

       migrations.AddField(
            model_name='Member',
            name='facebookId',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
       migrations.AddField(
            model_name='Member',
            name='twitterId',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
]
