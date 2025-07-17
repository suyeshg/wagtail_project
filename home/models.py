from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.blocks import (
    CharBlock, RichTextBlock, StructBlock, ListBlock, TextBlock
)
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField

# class HomePage(Page):
#     pass

class HeroSectionBlock(StructBlock):
    heading = CharBlock()
    subheading = CharBlock(required=False)
    background_image = ImageChooserBlock(required=False)

    class Meta:
        icon = "image"
        label = "Hero Section"

class TextImageBlock(StructBlock):
    title = CharBlock()
    text = RichTextBlock()
    image = ImageChooserBlock(required=False)
    image_position = CharBlock(default="left", help_text="left or right")

    class Meta:
        icon = "doc-full"
        label = "Text + Image Section"

class ValueItemBlock(StructBlock):
    icon = ImageChooserBlock(required=False, help_text="Upload an icon image")
    title = CharBlock()
    description = TextBlock()

class ValueSectionBlock(StructBlock):
    heading = CharBlock()
    items = ListBlock(ValueItemBlock())

    class Meta:
        icon = "list-ul"
        label = "Value Section"

class MilestoneBlock(StructBlock):
    year = CharBlock()
    title = CharBlock()
    description = TextBlock()

class MilestoneSectionBlock(StructBlock):
    heading = CharBlock()
    image = ImageChooserBlock(required=False, help_text="Image shown on left")
    milestones = ListBlock(MilestoneBlock())

    class Meta:
        icon = "date"
        label = "Milestone Section"

class TeamMemberBlock(StructBlock):
    name = CharBlock()
    role = CharBlock()
    bio = TextBlock()
    photo = ImageChooserBlock(required=False)

class TeamSectionBlock(StructBlock):
    heading = CharBlock()
    members = ListBlock(TeamMemberBlock())

    class Meta:
        icon = "user"
        label = "Team Section"

class LogoBlock(StructBlock):
    name = CharBlock()
    logo = ImageChooserBlock()

class LogoSectionBlock(StructBlock):
    heading = CharBlock()
    logos = ListBlock(LogoBlock())

    class Meta:
        icon = "image"
        label = "Logo / Awards Section"

class AboutUsPage(Page):
    body = StreamField(
        [
            ("hero_section", HeroSectionBlock()),
            ("text_image_section", TextImageBlock()),
            ("value_section", ValueSectionBlock()),
            ("milestone_section", MilestoneSectionBlock()),
            ("team_section", TeamSectionBlock()),
            ("logo_section", LogoSectionBlock()),
            ("rich_text", RichTextBlock()),
        ],
        use_json_field=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    api_fields = [
        APIField("body"),
    ]
