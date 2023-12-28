# Generated by Django 4.2.6 on 2023-12-21 00:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='FundraisingEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('fundraising_goal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('current_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.TextField()),
                ('contact_number', models.CharField(max_length=15)),
                ('certification_pdf', models.FileField(upload_to='certifications/')),
                ('is_approved', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, related_name='organizer_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='organizer_permissions', to='auth.permission')),
            ],
        ),
    ]
