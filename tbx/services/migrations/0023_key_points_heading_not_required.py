# Generated by Django 2.1.5 on 2019-03-15 13:23

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0022_servicepage_heading_for_processes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicepage',
            name='heading_for_key_points',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]