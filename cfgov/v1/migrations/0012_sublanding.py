# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailsnippets.blocks
import v1.models.snippets
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0011_auto_20151207_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='SublandingPage',
            fields=[
                ('cfgovpage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='v1.CFGOVPage')),
                ('header', wagtail.wagtailcore.fields.StreamField([(b'hero', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False))])), (b'background_color', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'link', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'is_button', wagtail.wagtailcore.blocks.BooleanBlock(required=False))])), (b'text_introduction', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), (b'intro', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False)), (b'has_rule', wagtail.wagtailcore.blocks.BooleanBlock(required=False))]))], blank=True)),
                ('content', wagtail.wagtailcore.fields.StreamField([(b'image_text_50_50_group', wagtail.wagtailcore.blocks.StructBlock([(b'image_texts', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(blank=True)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False))])), (b'is_widescreen', wagtail.wagtailcore.blocks.BooleanBlock(required=False, label=b'Use 16:9 image')), (b'is_button', wagtail.wagtailcore.blocks.BooleanBlock(required=False, label=b'Show links as button')), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False))])))])), (b'half_width_link_blob_group', wagtail.wagtailcore.blocks.StructBlock([(b'link_blobs', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(blank=True)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False))])))])), (b'heading', wagtail.wagtailcore.blocks.CharBlock(icon=b'title')), (b'well', wagtail.wagtailcore.blocks.StructBlock([(b'content', wagtail.wagtailcore.blocks.RichTextBlock(required=True, label=b'Well'))])), (b'table', wagtail.wagtailcore.blocks.StructBlock([(b'headers', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(max_length=20))), (b'rows', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StreamBlock([(b'hyperlink', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=20)), (b'text_blob', wagtail.wagtailcore.blocks.TextBlock()), (b'rich_text_blob', wagtail.wagtailcore.blocks.RichTextBlock())])))])), (b'contact', wagtail.wagtailcore.blocks.StructBlock([(b'header', wagtail.wagtailcore.blocks.CharBlock()), (b'body', wagtail.wagtailcore.blocks.RichTextBlock()), (b'contact', wagtail.wagtailsnippets.blocks.SnippetChooserBlock(v1.models.snippets.Contact))]))], blank=True)),
                ('sidebar_breakout', wagtail.wagtailcore.fields.StreamField([(b'slug', wagtail.wagtailcore.blocks.CharBlock(icon=b'title')), (b'heading', wagtail.wagtailcore.blocks.CharBlock(icon=b'title')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'edit')), (b'breakout_image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'is_round', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False, label=b'Round?')), (b'icon', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Enter icon class name.')), (b'heading', wagtail.wagtailcore.blocks.CharBlock(label=b'Introduction Heading')), (b'body', wagtail.wagtailcore.blocks.TextBlock(label=b'Introduction Body'))], heading=b'Breakout Image', icon=b'image')), (b'related_posts', wagtail.wagtailcore.blocks.StructBlock([(b'limit', wagtail.wagtailcore.blocks.CharBlock(default=b'3', label=b'Limit')), (b'relate_posts', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False, label=b'Blog Posts')), (b'relate_newsroom', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False, label=b'Newsroom')), (b'relate_events', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False, label=b'Events')), (b'view_more', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]))]))], blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('v1.cfgovpage',),
        ),
        migrations.AlterField(
            model_name='cfgovpage',
            name='sidefoot',
            field=wagtail.wagtailcore.fields.StreamField([(b'slug', wagtail.wagtailcore.blocks.CharBlock(icon=b'title')), (b'heading', wagtail.wagtailcore.blocks.CharBlock(icon=b'title')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'edit')), (b'hyperlink', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'call_to_action', wagtail.wagtailcore.blocks.StructBlock([(b'slug_text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), (b'paragraph_text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'button', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]))])), (b'related_posts', wagtail.wagtailcore.blocks.StructBlock([(b'limit', wagtail.wagtailcore.blocks.CharBlock(default=b'3', label=b'Limit')), (b'relate_posts', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False, label=b'Blog Posts')), (b'relate_newsroom', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False, label=b'Newsroom')), (b'relate_events', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False, label=b'Events')), (b'view_more', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]))])), (b'email_signup', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), (b'text', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'gd_code', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'form_field', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'btn_text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), (b'required', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'id', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), (b'info', wagtail.wagtailcore.blocks.RichTextBlock(required=False, label=b'Disclaimer')), (b'label', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), (b'type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'text', b'Text'), (b'checkbox', b'Checkbox'), (b'email', b'Email'), (b'number', b'Number'), (b'url', b'URL'), (b'radio', b'Radio')])), (b'placeholder', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False))]), required=False, icon=b'mail'))])), (b'contact', wagtail.wagtailcore.blocks.StructBlock([(b'header', wagtail.wagtailcore.blocks.CharBlock()), (b'body', wagtail.wagtailcore.blocks.RichTextBlock()), (b'contact', wagtail.wagtailsnippets.blocks.SnippetChooserBlock(v1.models.snippets.Contact))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_info',
            field=wagtail.wagtailcore.fields.StreamField([(b'email', wagtail.wagtailcore.blocks.StructBlock([(b'emails', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])))])), (b'phone', wagtail.wagtailcore.blocks.StructBlock([(b'fax', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False, label=b'Is this number a fax?')), (b'phones', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'number', wagtail.wagtailcore.blocks.CharBlock(max_length=15)), (b'vanity', wagtail.wagtailcore.blocks.CharBlock(max_length=15, required=False)), (b'tty', wagtail.wagtailcore.blocks.CharBlock(max_length=15, required=False))])))])), (b'address', wagtail.wagtailcore.blocks.StructBlock([(b'label', wagtail.wagtailcore.blocks.CharBlock(max_length=50)), (b'title', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'street', wagtail.wagtailcore.blocks.CharBlock(max_length=100)), (b'city', wagtail.wagtailcore.blocks.CharBlock(max_length=50)), (b'state', wagtail.wagtailcore.blocks.CharBlock(max_length=25)), (b'zip_code', wagtail.wagtailcore.blocks.CharBlock(max_length=15, required=False))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='demopage',
            name='molecules',
            field=wagtail.wagtailcore.fields.StreamField([(b'half_width_link_blob', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(blank=True)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False))])), (b'text_introduction', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), (b'intro', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'link', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'has_rule', wagtail.wagtailcore.blocks.BooleanBlock(required=False))])), (b'image_text_2575', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(required=False))])), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False)), (b'has_rule', wagtail.wagtailcore.blocks.BooleanBlock(required=False))])), (b'image_text_5050', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(blank=True)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False))])), (b'is_widescreen', wagtail.wagtailcore.blocks.BooleanBlock(required=False, label=b'Use 16:9 image')), (b'is_button', wagtail.wagtailcore.blocks.BooleanBlock(required=False, label=b'Show links as button')), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False))])), (b'hero', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False))])), (b'background_color', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'link', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'is_button', wagtail.wagtailcore.blocks.BooleanBlock(required=False))])), (b'formfield_with_button', wagtail.wagtailcore.blocks.StructBlock([(b'btn_text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), (b'required', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'id', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), (b'info', wagtail.wagtailcore.blocks.RichTextBlock(required=False, label=b'Disclaimer')), (b'label', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), (b'type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'text', b'Text'), (b'checkbox', b'Checkbox'), (b'email', b'Email'), (b'number', b'Number'), (b'url', b'URL'), (b'radio', b'Radio')])), (b'placeholder', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False))])), (b'call_to_action', wagtail.wagtailcore.blocks.StructBlock([(b'slug_text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), (b'paragraph_text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'button', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='demopage',
            name='organisms',
            field=wagtail.wagtailcore.fields.StreamField([(b'well', wagtail.wagtailcore.blocks.StructBlock([(b'content', wagtail.wagtailcore.blocks.RichTextBlock(required=True, label=b'Well'))])), (b'full_width_text', wagtail.wagtailcore.blocks.StructBlock([(b'content', wagtail.wagtailcore.blocks.RichTextBlock(required=True))])), (b'post_preview', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False))])), (b'post', wagtail.wagtailcore.blocks.PageChooserBlock(required=True)), (b'link', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='half_width_link_blob_content',
            field=wagtail.wagtailcore.fields.StreamField([(b'half_width_link_blob', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(blank=True)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False))]))], verbose_name=b'content', blank=True),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='hero',
            field=wagtail.wagtailcore.fields.StreamField([(b'hero', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False))])), (b'background_color', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'link', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'is_button', wagtail.wagtailcore.blocks.BooleanBlock(required=False))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='image_text_25_75_content',
            field=wagtail.wagtailcore.fields.StreamField([(b'image_text_25_75', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(required=False))])), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False)), (b'has_rule', wagtail.wagtailcore.blocks.BooleanBlock(required=False))]))], verbose_name=b'content', blank=True),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='image_text_50_50_content',
            field=wagtail.wagtailcore.fields.StreamField([(b'image_text_50_50', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(blank=True)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False))])), (b'is_widescreen', wagtail.wagtailcore.blocks.BooleanBlock(required=False, label=b'Use 16:9 image')), (b'is_button', wagtail.wagtailcore.blocks.BooleanBlock(required=False, label=b'Show links as button')), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False))]))], verbose_name=b'content', blank=True),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='introduction',
            field=wagtail.wagtailcore.fields.StreamField([(b'text_introduction', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), (b'intro', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'link', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'has_rule', wagtail.wagtailcore.blocks.BooleanBlock(required=False))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='wells',
            field=wagtail.wagtailcore.fields.StreamField([(b'well', wagtail.wagtailcore.blocks.StructBlock([(b'content', wagtail.wagtailcore.blocks.RichTextBlock(required=True, label=b'Well'))]))], blank=True),
        ),
    ]
