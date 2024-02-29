# Generated by Django 4.2.5 on 2024-02-29 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FilledRiverBank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geobag_counting_riverbank_img', models.ImageField(default='No images', upload_to='Geobag_at_RiverBank_img/')),
                ('counting_figure_text', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='GeobagRiverBank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geobag_at_riverbank_img', models.ImageField(default='No images', upload_to='Geobag_at_RiverBank_img/')),
                ('image_figure_text', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='PreparingDataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preparing_pataset_img', models.ImageField(default='No images', upload_to='Geobag_at_RiverBank_img/')),
                ('preparing_dataset_figure_text', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='PrototypeProposed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prototype_of_proposed_img', models.ImageField(default='No images', upload_to='Geobag_at_RiverBank_img/')),
                ('proposed_figure_text', models.CharField(default='Default value', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TestingProcedures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testing_procedures_img', models.ImageField(default='No images', upload_to='Geobag_at_RiverBank_img/')),
                ('testing_procedures_figure_text', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ToonificationHeading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toonification_heading', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ToonificationImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toonification_photo', models.ImageField(default='No images', upload_to='ToonificationImage/')),
            ],
        ),
    ]
