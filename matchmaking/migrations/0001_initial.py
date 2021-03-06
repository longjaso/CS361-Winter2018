# Generated by Django 2.0.2 on 2018-03-02 06:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=16, null=True)),
                ('email', models.CharField(max_length=256)),
                ('website', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('sex', models.CharField(max_length=16)),
                ('age', models.IntegerField()),
                ('breed', models.CharField(max_length=256, null=True)),
                ('bio', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=256)),
                ('state', models.CharField(choices=[('AL', 'AL'), ('AK', 'AK'), ('AZ', 'AZ'), ('AR', 'AR'), ('CA', 'CA'), ('CO', 'CO'), ('CT', 'CT'), ('DC', 'DC'), ('DE', 'DE'), ('FL', 'FL'), ('GA', 'GA'), ('HI', 'HI'), ('ID', 'ID'), ('IL', 'IL'), ('IN', 'IN'), ('IA', 'IA'), ('KS', 'KS'), ('KY', 'KY'), ('LA', 'LA'), ('ME', 'ME'), ('MD', 'MD'), ('MA', 'MA'), ('MI', 'MI'), ('MN', 'MN'), ('MS', 'MS'), ('MO', 'MO'), ('MT', 'MT'), ('NE', 'NE'), ('NV', 'NV'), ('NH', 'NH'), ('NJ', 'NJ'), ('NM', 'NM'), ('NY', 'NY'), ('NC', 'NC'), ('ND', 'ND'), ('OH', 'OH'), ('OK', 'OK'), ('OR', 'OR'), ('PA', 'PA'), ('RI', 'RI'), ('SC', 'SC'), ('SD', 'SD'), ('TN', 'TN'), ('TX', 'TX'), ('UT', 'UT'), ('VT', 'VT'), ('VA', 'VA'), ('WA', 'WA'), ('WV', 'WV'), ('WI', 'WI'), ('WY', 'WY')], max_length=2)),
                ('zipcode', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalityQualities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friendly', models.BooleanField(default=False)),
                ('kid_friendly', models.BooleanField(default=False)),
                ('likes_water', models.BooleanField(default=False)),
                ('likes_cars', models.BooleanField(default=False)),
                ('socialized', models.BooleanField(default=False)),
                ('rescue_animal', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalQualities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=64, null=True)),
                ('height', models.FloatField(null=True)),
                ('weight', models.FloatField(null=True)),
                ('eye_color', models.CharField(max_length=64, null=True)),
                ('hypoallergenic', models.BooleanField(default=False)),
                ('shedding', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('verified', models.BooleanField(default=False)),
                ('contact_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matchmaking.ContactInfo')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matchmaking.Location')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matchmaking.ContactInfo')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='matchmaking.Location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='shelter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matchmaking.Shelter'),
        ),
        migrations.AddField(
            model_name='payment',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matchmaking.UserProfile'),
        ),
        migrations.AddField(
            model_name='message',
            name='user_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_from', to='matchmaking.UserProfile'),
        ),
        migrations.AddField(
            model_name='message',
            name='user_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_to', to='matchmaking.UserProfile'),
        ),
        migrations.AddField(
            model_name='dog',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matchmaking.Location'),
        ),
        migrations.AddField(
            model_name='dog',
            name='personality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matchmaking.PersonalityQualities'),
        ),
        migrations.AddField(
            model_name='dog',
            name='physical',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matchmaking.PhysicalQualities'),
        ),
    ]
