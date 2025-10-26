from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.snippets.models import register_snippet
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

from .blocks import HeroBannerBlock, NavbarBlock


@register_snippet
class HeroBanner(models.Model):
    """
    A reusable hero banner section that can be added to any page.
    Includes a StreamField using HeroBannerBlock for full control.
    """

    title = models.CharField(
        max_length=255,
        help_text="The title of the banner (for admin reference)"
    )

    content = StreamField(
        [
            ("hero", HeroBannerBlock()),
            # Removed SimpleHeroBannerBlock
        ],
        use_json_field=True,
        blank=True,
        verbose_name="Hero Banner Content"
    )

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    panels = [
        FieldPanel("title"),
        FieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Hero Banner"
        verbose_name_plural = "Hero Banners"
        ordering = ["-updated_at"]

    def __str__(self):
        return str(self.title)


class HomePage(Page):
    """
    Custom Home Page model that connects to the Hero Banner snippet.
    """

    navbar = StreamField([
        ('navbar', NavbarBlock()),
    ], use_json_field=True, blank=True, verbose_name="Navigation Bar")

    hero_section = models.ForeignKey(
        "home.HeroBanner",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="homepages",
        help_text="Select a hero banner to display on this page."
    )

    # Add a StreamField for additional content
    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', blocks.StructBlock([
            ('image', ImageChooserBlock()),
            ('caption', blocks.CharBlock(required=False)),
        ])),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("navbar"),
        FieldPanel("hero_section"),
        FieldPanel("body"),
    ]

    class Meta(Page.Meta):
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"

    # Optional: Add context to render hero block data easily
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["navbar"] = self.navbar
        context["hero_section"] = self.hero_section
        return context