from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='company.language')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='company.company')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='company.tag')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='company.company')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='company.language')),
            ],
        ),
    ]
