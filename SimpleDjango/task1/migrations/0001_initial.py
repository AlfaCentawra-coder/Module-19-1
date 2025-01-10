
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='username аккаунта', max_length=100)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=7)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=7)),
                ('size', models.DecimalField(decimal_places=3, max_digits=7)),
                ('description', models.TextField()),
                ('age_limited', models.BooleanField(default=False)),
                ('buyer', models.ManyToManyField(related_name='username', to='task1.buyer')),
            ],
        ),
    ]
