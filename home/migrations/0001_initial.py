# Generated by Django 3.1.1 on 2020-10-26 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=30)),
                ('doc_dob', models.CharField(max_length=30)),
                ('doc_age', models.CharField(max_length=30)),
                ('doc_gender', models.CharField(max_length=30)),
                ('doc_contact', models.CharField(max_length=30)),
                ('doc_email', models.EmailField(max_length=254)),
                ('doc_address', models.CharField(max_length=100)),
                ('doc_degree', models.CharField(max_length=300)),
                ('doc_desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('dob', models.DateField(default='', editable=False)),
                ('age', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('doctor', models.CharField(max_length=30, null=True)),
                ('desc', models.CharField(max_length=200, null=True)),
                ('date', models.DateField(default='', editable=False)),
                ('time', models.TimeField(default='', editable=False)),
                ('status', models.CharField(max_length=500)),
                ('details', models.TextField(default='Date:\nReason for visit:\nPrescription:\nTests:\nSummary:\nNext visit:', max_length=2048)),
            ],
        ),
    ]