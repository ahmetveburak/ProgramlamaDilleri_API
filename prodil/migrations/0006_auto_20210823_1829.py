# Generated by Django 3.2.4 on 2021-08-23 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodil', '0005_auto_20210820_2356'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='botuser',
            options={'ordering': ('user_id',)},
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='author',
            name='site',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Web Site'),
        ),
        migrations.AlterField(
            model_name='botuser',
            name='first_name',
            field=models.CharField(max_length=70, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='botuser',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=70, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='botuser',
            name='user_id',
            field=models.CharField(max_length=100, verbose_name='Telegram User ID'),
        ),
        migrations.AlterField(
            model_name='botuser',
            name='username',
            field=models.CharField(blank=True, default='', max_length=40, verbose_name='Username'),
        ),
        migrations.AlterField(
            model_name='category',
            name='enabled',
            field=models.BooleanField(verbose_name='Is Enabled?'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Programming Language Name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='order',
            field=models.IntegerField(verbose_name='Order'),
        ),
    ]
