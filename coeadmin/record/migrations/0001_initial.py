# Generated by Django 2.2.12 on 2022-01-04 05:11

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('contact_date', models.DateField()),
                ('contact_type', models.CharField(max_length=100)),
                ('insolation_days', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=False, verbose_name='active_status')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('document', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(message='You must enter a DNI number without points.', regex='\\d{8,8}$')])),
                ('date_birth', models.DateField()),
                ('gender', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Positive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('positivity_date', models.DateField()),
                ('variant_type', models.CharField(max_length=100)),
                ('laboratory', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True, verbose_name='active_status')),
                ('contacts', models.ManyToManyField(related_name='contacts', through='record.Contact', to='record.Person')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positive', to='record.Person')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('latitude', models.FloatField(default=0)),
                ('longitude', models.FloatField(default=0)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='record.Person')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Isolation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('isolation_date', models.DateField(blank=True, null=True)),
                ('days_isolation', models.IntegerField(default=0)),
                ('high_insulation', models.BooleanField(default=False)),
                ('high_insulation_date', models.DateField(blank=True, null=True)),
                ('positivity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='record.Positive')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='contact',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='record.Person'),
        ),
        migrations.AddField(
            model_name='contact',
            name='positive',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='record.Positive'),
        ),
    ]