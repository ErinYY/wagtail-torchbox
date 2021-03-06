# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-24 08:45


from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('torchbox', '0074_servicepage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicepage',
            name='streamfield',
            field=wagtail.core.fields.StreamField([(b'case_studies', wagtail.core.blocks.StructBlock([(b'title', wagtail.core.blocks.CharBlock(required=True)), (b'intro', wagtail.core.blocks.TextBlock(required=True)), (b'case_studies', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock(['torchbox.WorkPage'])))])), (b'highlights', wagtail.core.blocks.StructBlock([(b'title', wagtail.core.blocks.CharBlock(required=True)), (b'intro', wagtail.core.blocks.TextBlock(required=True)), (b'highlights', wagtail.core.blocks.ListBlock(wagtail.core.blocks.TextBlock()))])), (b'pull_quote', wagtail.core.blocks.StructBlock([(b'quote', wagtail.core.blocks.CharBlock(classname='quote title')), (b'attribution', wagtail.core.blocks.CharBlock())], template='blocks/pull_quote_block.html')), (b'process', wagtail.core.blocks.StructBlock([(b'title', wagtail.core.blocks.CharBlock(required=True)), (b'intro', wagtail.core.blocks.TextBlock(required=True)), (b'steps', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('icon', wagtail.core.blocks.CharBlock(help_text='Paste SVG code here', max_length=9000, required=True)), ('description', wagtail.core.blocks.TextBlock(required=True))])))])), (b'people', wagtail.core.blocks.StructBlock([(b'title', wagtail.core.blocks.CharBlock(required=True)), (b'intro', wagtail.core.blocks.TextBlock(required=True)), (b'people', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock()))]))]),
        ),
    ]
