from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from django.template.loader import render_to_string


# ---------- REUSABLE CTA BUTTON ----------
class CTAButtonBlock(blocks.StructBlock):
    label = blocks.CharBlock(max_length=60, required=True)
    url = blocks.URLBlock(required=True)
    icon = blocks.CharBlock(required=False)
    style = blocks.ChoiceBlock(
        choices=[
            ("primary", "Primary"),
            ("secondary", "Secondary"),
            ("outline", "Outline"),
            ("ghost", "Ghost"),
            ("gradient", "Gradient"),
            ("glass", "Glass Effect"),
            ("link", "Text Link"),
        ],
        default="primary",
    )
    hover_effect = blocks.ChoiceBlock(
        choices=[
            ("none", "None"),
            ("grow", "Grow"),
            ("shrink", "Shrink"),
            ("underline", "Underline"),
            ("shadow", "Shadow Glow"),
            ("pulse", "Pulse"),
            ("tilt", "Tilt"),
        ],
        default="none",
    )
    open_in_new_tab = blocks.BooleanBlock(required=False, default=False)
    gradient_start = blocks.CharBlock(required=False, help_text="Used if style=gradient")
    gradient_end = blocks.CharBlock(required=False)
    gradient_angle = blocks.CharBlock(required=False, default="45deg")
    glow_color = blocks.CharBlock(required=False, default="#FFD700")
    
    # Dimension controls
    width = blocks.CharBlock(required=False, help_text="Button width (e.g. 200px, 100%)")
    height = blocks.CharBlock(required=False, help_text="Button height (e.g. 50px)")
    min_width = blocks.CharBlock(required=False, help_text="Minimum width (e.g. 150px)")
    min_height = blocks.CharBlock(required=False, help_text="Minimum height (e.g. 40px)")
    max_width = blocks.CharBlock(required=False, help_text="Maximum width (e.g. 300px)")
    max_height = blocks.CharBlock(required=False, help_text="Maximum height (e.g. 60px)")
    
    # Styling controls
    border_radius = blocks.CharBlock(required=False, default="8px", help_text="Border radius (e.g. 5px, 50%)")
    border_width = blocks.CharBlock(required=False, default="2px", help_text="Border width (e.g. 1px)")
    border_style = blocks.ChoiceBlock(
        choices=[
            ("solid", "Solid"),
            ("dashed", "Dashed"),
            ("dotted", "Dotted"),
            ("double", "Double"),
            ("none", "None"),
        ],
        default="solid",
        required=False
    )
    border_color = blocks.CharBlock(required=False, help_text="Border color (e.g. #000000)")
    padding = blocks.CharBlock(required=False, default="0.9rem 1.8rem", help_text="Padding (e.g. 10px 20px)")
    margin = blocks.CharBlock(required=False, help_text="Margin (e.g. 10px 0)")
    font_size = blocks.CharBlock(required=False, default="1rem", help_text="Font size (e.g. 16px)")
    font_weight = blocks.ChoiceBlock(
        choices=[
            ("300", "Light"),
            ("400", "Regular"),
            ("500", "Medium"),
            ("600", "Semi-Bold"),
            ("700", "Bold"),
        ],
        default="600",
        required=False
    )
    text_transform = blocks.ChoiceBlock(
        choices=[
            ("none", "None"),
            ("uppercase", "Uppercase"),
            ("lowercase", "Lowercase"),
            ("capitalize", "Capitalize"),
        ],
        default="none",
        required=False
    )
    letter_spacing = blocks.CharBlock(required=False, help_text="Letter spacing (e.g. 1px)")
    
    # Advanced styling
    custom_css = blocks.TextBlock(required=False, help_text="Custom CSS styles (e.g. box-shadow: 2px 2px 5px rgba(0,0,0,0.3);)")
    
    def render(self, value, context=None):
        return render_to_string("blocks/cta_button_block.html", {"self": value})


# ---------- HERO BANNER ----------
class HeroBannerBlock(blocks.StructBlock):
    # Background
    background_type = blocks.ChoiceBlock(
        choices=[
            ("image", "Image"),
            ("color", "Solid Color"),
            ("gradient", "Gradient"),
            ("video", "Video"),
            ("kenburns", "Ken Burns Zoom"),
        ],
        default="image",
    )
    background_image = ImageChooserBlock(required=False)
    background_image_url = blocks.URLBlock(required=False)
    background_video_url = blocks.URLBlock(required=False)
    background_color = blocks.CharBlock(required=False)
    gradient_start = blocks.CharBlock(required=False)
    gradient_end = blocks.CharBlock(required=False)
    gradient_direction = blocks.CharBlock(required=False, default="to right")
    overlay_enabled = blocks.BooleanBlock(required=False, default=True)
    overlay_color = blocks.CharBlock(required=False, default="rgba(0,0,0,0.3)")
    overlay_opacity = blocks.FloatBlock(required=False, default=0.5)
    overlay_blur = blocks.FloatBlock(required=False, default=0.0)
    blur_intensity = blocks.FloatBlock(required=False, default=0.0)

    # Content
    title = blocks.CharBlock(required=True, max_length=140)
    subtitle = blocks.CharBlock(required=False, max_length=250)
    tagline = blocks.TextBlock(required=False)

    # Typography
    title_font_size = blocks.CharBlock(required=False, default="clamp(2rem,5vw,4rem)")
    subtitle_font_size = blocks.CharBlock(required=False, default="1.25rem")
    tagline_font_size = blocks.CharBlock(required=False, default="1rem")
    title_color = blocks.CharBlock(required=False, default="#ffffff")
    subtitle_color = blocks.CharBlock(required=False, default="#f5f5f5")
    tagline_color = blocks.CharBlock(required=False, default="#dddddd")
    font_family = blocks.CharBlock(required=False, help_text="Optional custom font family")
    font_weight = blocks.ChoiceBlock(
        choices=[
            ("300", "Light"),
            ("400", "Regular"),
            ("500", "Medium"),
            ("600", "Semi-Bold"),
            ("700", "Bold"),
        ],
        default="600",
    )
    letter_spacing = blocks.CharBlock(required=False, default="0px")
    text_shadow = blocks.BooleanBlock(required=False, default=False)

    # Layout
    vertical_alignment = blocks.ChoiceBlock(
        choices=[("top", "Top"), ("center", "Center"), ("bottom", "Bottom")],
        default="center",
    )
    horizontal_alignment = blocks.ChoiceBlock(
        choices=[("left", "Left"), ("center", "Center"), ("right", "Right")],
        default="center",
    )
    content_max_width = blocks.CharBlock(required=False, default="900px")
    content_padding = blocks.CharBlock(required=False, default="8rem 2rem")
    full_height = blocks.BooleanBlock(required=False, default=True)
    aspect_ratio = blocks.CharBlock(required=False, default="16/9")
    parallax = blocks.BooleanBlock(required=False, default=False)
    scroll_parallax_strength = blocks.FloatBlock(required=False, default=0.3)
    
    # Dimension controls
    width = blocks.CharBlock(required=False, help_text="Banner width (e.g. 100%, 1200px)")
    height = blocks.CharBlock(required=False, help_text="Banner height (e.g. 500px, 60vh)")
    min_height = blocks.CharBlock(required=False, help_text="Minimum height (e.g. 400px)")
    max_height = blocks.CharBlock(required=False, help_text="Maximum height (e.g. 800px)")
    
    # Styling controls
    border_radius = blocks.CharBlock(required=False, help_text="Border radius (e.g. 10px)")
    border_width = blocks.CharBlock(required=False, default="0px", help_text="Border width (e.g. 2px)")
    border_style = blocks.ChoiceBlock(
        choices=[
            ("solid", "Solid"),
            ("dashed", "Dashed"),
            ("dotted", "Dotted"),
            ("double", "Double"),
            ("none", "None"),
        ],
        default="none",
        required=False
    )
    border_color = blocks.CharBlock(required=False, help_text="Border color (e.g. #000000)")
    margin = blocks.CharBlock(required=False, help_text="Margin (e.g. 20px 0)")
    
    # Buttons
    ctas = blocks.ListBlock(CTAButtonBlock(), required=False, max_num=4)
    button_alignment = blocks.ChoiceBlock(
        choices=[("left", "Left"), ("center", "Center"), ("right", "Right")],
        default="center",
    )
    button_spacing = blocks.CharBlock(required=False, default="1rem")

    # Animations
    text_animation = blocks.ChoiceBlock(
        choices=[
            ("none", "None"),
            ("fade", "Fade In"),
            ("slide-up", "Slide Up"),
            ("slide-left", "Slide Left"),
            ("typewriter", "Typewriter"),
            ("zoom", "Zoom In"),
            ("kenburns", "Ken Burns"),
        ],
        default="fade",
    )
    animation_duration = blocks.CharBlock(required=False, default="1s")
    animation_delay = blocks.CharBlock(required=False, default="0s")
    animation_loop = blocks.BooleanBlock(required=False, default=False)
    entry_effect = blocks.ChoiceBlock(
        choices=[
            ("none", "None"),
            ("blur-in", "Blur In"),
            ("glow", "Glow Fade"),
            ("split-text", "Split Text Reveal"),
        ],
        default="none",
    )

    # Mobile overrides
    mobile_background_image = ImageChooserBlock(required=False)
    mobile_background_image_url = blocks.URLBlock(required=False)
    mobile_hide_overlay = blocks.BooleanBlock(required=False, default=False)
    mobile_title_size = blocks.CharBlock(required=False)
    mobile_padding = blocks.CharBlock(required=False, default="4rem 1.5rem")

    # Interactivity
    scroll_indicator = blocks.BooleanBlock(required=False, default=False)
    scroll_down_target = blocks.CharBlock(required=False, help_text="Optional section ID to scroll to.")
    auto_scroll = blocks.BooleanBlock(required=False, default=False)
    scroll_delay = blocks.IntegerBlock(required=False, default=5)
    mouse_parallax_effect = blocks.BooleanBlock(required=False, default=False)
    hover_glow = blocks.BooleanBlock(required=False, default=False)

    # Custom
    theme = blocks.ChoiceBlock(
        choices=[
            ("dark", "Dark"),
            ("light", "Light"),
            ("gold", "Gold Accent"),
            ("auremont", "Auremont Classic"),
        ],
        default="auremont",
    )
    css_class = blocks.CharBlock(required=False)
    custom_id = blocks.CharBlock(required=False)
    custom_css = blocks.TextBlock(required=False)
    custom_js = blocks.TextBlock(required=False)

    def render(self, value, context=None):
        return render_to_string("blocks/hero_banner_block.html", {"self": value})


# ---------- NAVBAR SEARCH ----------
class NavbarSearchBlock(blocks.StructBlock):
    placeholder_text = blocks.CharBlock(
        required=False, 
        default="Search...",
        help_text="Placeholder text for the search input"
    )
    search_endpoint_url = blocks.URLBlock(
        required=False, 
        default="/search/",
        help_text="URL endpoint for search requests"
    )
    enable_toggle = blocks.BooleanBlock(
        required=False, 
        default=True,
        help_text="Enable toggle behavior (compact icon that expands to input field)"
    )
    enable_auto_suggest = blocks.BooleanBlock(
        required=False, 
        default=False,
        help_text="Enable auto-suggest dropdown powered by AJAX"
    )
    auto_suggest_endpoint = blocks.URLBlock(
        required=False, 
        help_text="URL endpoint for auto-suggest AJAX requests"
    )
    
    # Styling options
    input_width = blocks.CharBlock(
        required=False, 
        help_text="Width of the search input when expanded (e.g. 200px, 100%)"
    )
    input_height = blocks.CharBlock(
        required=False, 
        help_text="Height of the search input (e.g. 40px)"
    )
    border_radius = blocks.CharBlock(
        required=False, 
        default="4px",
        help_text="Border radius of the search input (e.g. 5px, 50%)"
    )
    border_width = blocks.CharBlock(
        required=False, 
        default="1px",
        help_text="Border width of the search input (e.g. 1px)"
    )
    border_color = blocks.CharBlock(
        required=False, 
        default="#CCCCCC",
        help_text="Border color of the search input (e.g. #000000)"
    )
    focus_border_color = blocks.CharBlock(
        required=False, 
        default="#D4AF37",
        help_text="Border color when input is focused (e.g. #D4AF37 for gold)"
    )
    background_color = blocks.CharBlock(
        required=False, 
        default="#FFFFFF",
        help_text="Background color of the search input (e.g. #FFFFFF)"
    )
    text_color = blocks.CharBlock(
        required=False, 
        default="#000000",
        help_text="Text color of the search input (e.g. #000000)"
    )
    icon_color = blocks.CharBlock(
        required=False, 
        default="#666666",
        help_text="Color of the search icon (e.g. #666666)"
    )
    
    def render(self, value, context=None):
        return render_to_string("blocks/navbar_search_block.html", {"self": value})


# ---------- USER MENU ----------
class UserMenuBlock(blocks.StructBlock):
    # Authentication links
    login_link = blocks.URLBlock(
        required=False, 
        default="/accounts/login/",
        help_text="URL for login page"
    )
    register_link = blocks.URLBlock(
        required=False, 
        default="/accounts/register/",
        help_text="URL for registration page"
    )
    
    # Dropdown menu items for logged-in users
    profile_link = blocks.URLBlock(
        required=False, 
        default="/accounts/profile/",
        help_text="URL for user profile page"
    )
    settings_link = blocks.URLBlock(
        required=False, 
        default="/accounts/settings/",
        help_text="URL for user settings page"
    )
    logout_link = blocks.URLBlock(
        required=False, 
        default="/accounts/logout/",
        help_text="URL for logout functionality"
    )
    
    # Display options
    show_avatar = blocks.BooleanBlock(
        required=False, 
        default=True,
        help_text="Show user avatar if available"
    )
    avatar_fallback = blocks.ChoiceBlock(
        choices=[
            ("initials", "User Initials"),
            ("icon", "Default Icon"),
            ("none", "No Fallback"),
        ],
        default="initials",
        help_text="Fallback display when no avatar is available"
    )
    avatar_size = blocks.CharBlock(
        required=False, 
        default="40px",
        help_text="Size of the avatar (e.g. 40px, 2.5rem)"
    )
    avatar_border_radius = blocks.CharBlock(
        required=False, 
        default="50%",
        help_text="Border radius of the avatar (e.g. 50% for circle, 4px for rounded)"
    )
    
    # Styling options
    dropdown_width = blocks.CharBlock(
        required=False, 
        default="200px",
        help_text="Width of the dropdown menu (e.g. 200px, 15rem)"
    )
    dropdown_background = blocks.CharBlock(
        required=False, 
        default="#FFFFFF",
        help_text="Background color of the dropdown menu"
    )
    dropdown_text_color = blocks.CharBlock(
        required=False, 
        default="#333333",
        help_text="Text color of the dropdown menu"
    )
    dropdown_hover_background = blocks.CharBlock(
        required=False, 
        default="#F5F5F5",
        help_text="Background color on hover"
    )
    dropdown_border_radius = blocks.CharBlock(
        required=False, 
        default="8px",
        help_text="Border radius of the dropdown menu"
    )
    dropdown_shadow = blocks.CharBlock(
        required=False, 
        default="0 4px 6px rgba(0,0,0,0.1)",
        help_text="Box shadow for the dropdown menu"
    )
    
    def render(self, value, context=None):
        # Pass the request context to detect user session
        if context and 'request' in context:
            context['user'] = context['request'].user
        return render_to_string("blocks/user_menu_block.html", {"self": value, "context": context})


# ---------- NAVBAR ----------
class DropdownItem(blocks.StructBlock):
    label = blocks.CharBlock(required=True)
    link = blocks.URLBlock(required=True)
    icon_class = blocks.CharBlock(required=False)
    description = blocks.CharBlock(required=False, help_text="Optional short text for mega-menu style")


class MegaMenuLinkBlock(blocks.StructBlock):
    label = blocks.CharBlock(required=True, max_length=50)
    url = blocks.URLBlock(required=True)
    icon_class = blocks.CharBlock(required=False, help_text="Optional icon class (e.g. fa-solid fa-book)")


class MegaMenuColumnBlock(blocks.StructBlock):
    column_title = blocks.CharBlock(required=False, max_length=50)
    links = blocks.ListBlock(MegaMenuLinkBlock(), required=True, max_num=10)
    icon_class = blocks.CharBlock(required=False, help_text="Optional icon for the column")


class MegaMenuItemBlock(blocks.StructBlock):
    label = blocks.CharBlock(required=True, max_length=50)
    link = blocks.URLBlock(required=False, help_text="Optional link for the main menu item")
    mega_menu_columns = blocks.ListBlock(MegaMenuColumnBlock(), required=False, max_num=4, help_text="Up to 4 columns for mega menu")
    icon_class = blocks.CharBlock(required=False, help_text="Optional icon for the menu item")
    is_mega_menu = blocks.BooleanBlock(required=False, default=False, help_text="Enable mega menu for this item")


# ---------- LANGUAGE SWITCHER ----------
class LanguageItemBlock(blocks.StructBlock):
    code = blocks.CharBlock(
        required=True,
        max_length=10,
        help_text="Language code (e.g. 'en', 'es', 'fr')"
    )
    label = blocks.CharBlock(
        required=True,
        max_length=50,
        help_text="Language label (e.g. 'English', 'Español', 'Français')"
    )
    flag_icon = blocks.CharBlock(
        required=False,
        max_length=50,
        help_text="Flag icon class (e.g. 'fi fi-us', 'fi fi-es', 'fi fi-fr')"
    )


class LanguageSwitcherBlock(blocks.StructBlock):
    available_languages = blocks.ListBlock(
        LanguageItemBlock(),
        required=True,
        help_text="List of available languages"
    )
    default_language = blocks.CharBlock(
        required=False,
        max_length=10,
        help_text="Default language code (e.g. 'en')"
    )
    
    # Styling options
    dropdown_width = blocks.CharBlock(
        required=False,
        default="150px",
        help_text="Width of the dropdown menu (e.g. 150px, 12rem)"
    )
    dropdown_background = blocks.CharBlock(
        required=False,
        default="#FFFFFF",
        help_text="Background color of the dropdown menu"
    )
    dropdown_text_color = blocks.CharBlock(
        required=False,
        default="#333333",
        help_text="Text color of the dropdown menu"
    )
    dropdown_hover_background = blocks.CharBlock(
        required=False,
        default="#F5F5F5",
        help_text="Background color on hover"
    )
    dropdown_border_radius = blocks.CharBlock(
        required=False,
        default="8px",
        help_text="Border radius of the dropdown menu"
    )
    dropdown_shadow = blocks.CharBlock(
        required=False,
        default="0 4px 6px rgba(0,0,0,0.1)",
        help_text="Box shadow for the dropdown menu"
    )
    
    # Animation options
    animation_duration = blocks.CharBlock(
        required=False,
        default="0.3s",
        help_text="Duration of animations (e.g. 0.3s, 300ms)"
    )
    animation_easing = blocks.CharBlock(
        required=False,
        default="ease-in-out",
        help_text="Easing function for animations"
    )
    
    def render(self, value, context=None):
        # Pass the request context for i18n integration
        if context and 'request' in context:
            context['current_language'] = context['request'].LANGUAGE_CODE
        return render_to_string("blocks/language_switcher_block.html", {"self": value, "context": context})


class MenuItem(blocks.StructBlock):
    label = blocks.CharBlock(required=True)
    link = blocks.URLBlock(required=False)
    dropdown_items = blocks.ListBlock(DropdownItem(), required=False)
    icon_class = blocks.CharBlock(required=False)
    hover_effect = blocks.ChoiceBlock(
        choices=[
            ("none", "None"),
            ("glow", "Glow"),
            ("underline", "Underline"),
            ("gold-underline", "Gold Underline"),
            ("scale", "Scale Up"),
            ("slide-bg", "Slide Background"),
        ],
        default="gold-underline",
    )
    is_button = blocks.BooleanBlock(required=False, default=False)
    button_style = blocks.ChoiceBlock(
        choices=[("primary", "Primary"), ("outline", "Outline"), ("ghost", "Ghost")],
        default="primary",
    )
    
    # Dimension controls
    width = blocks.CharBlock(required=False, help_text="Menu item width (e.g. 120px, auto)")
    height = blocks.CharBlock(required=False, help_text="Menu item height (e.g. 50px)")
    
    # Styling controls
    padding = blocks.CharBlock(required=False, help_text="Padding (e.g. 10px 15px)")
    margin = blocks.CharBlock(required=False, help_text="Margin (e.g. 0 5px)")
    font_size = blocks.CharBlock(required=False, help_text="Font size (e.g. 16px)")
    font_weight = blocks.ChoiceBlock(
        choices=[
            ("300", "Light"),
            ("400", "Regular"),
            ("500", "Medium"),
            ("600", "Semi-Bold"),
            ("700", "Bold"),
        ],
        default="500",
        required=False
    )


class NavbarBlock(blocks.StructBlock):
    # Branding
    logo_image = ImageChooserBlock(required=False)
    university_name = blocks.CharBlock(required=True, default="Auremont University")
    tagline = blocks.CharBlock(required=False)
    logo_alignment = blocks.ChoiceBlock(
        choices=[("left", "Left"), ("center", "Center"), ("right", "Right")],
        default="left",
    )

    # Menu
    menu_items = blocks.ListBlock(MegaMenuItemBlock(), required=False)
    menu_alignment = blocks.ChoiceBlock(
        choices=[("left", "Left"), ("center", "Center"), ("right", "Right")],
        default="right",
    )
    enable_search = blocks.BooleanBlock(required=False, default=True)
    search_settings = NavbarSearchBlock(required=False)
    enable_user_menu = blocks.BooleanBlock(required=False, default=True)
    user_menu_settings = UserMenuBlock(required=False)
    enable_language_switcher = blocks.BooleanBlock(required=False, default=False)
    language_switcher_settings = LanguageSwitcherBlock(required=False)

    # Appearance
    background_color = blocks.CharBlock(required=False, default="#001F3F")
    text_color = blocks.CharBlock(required=False, default="#FFFFFF")
    hover_color = blocks.CharBlock(required=False, default="#FFD700")
    gradient_background = blocks.BooleanBlock(required=False, default=False)
    gradient_start = blocks.CharBlock(required=False, default="#001F3F")
    gradient_end = blocks.CharBlock(required=False, default="#003366")
    backdrop_blur = blocks.BooleanBlock(required=False, default=False)
    blur_strength = blocks.FloatBlock(required=False, default=10.0)
    transparent_on_load = blocks.BooleanBlock(required=False, default=True)
    nav_shadow = blocks.BooleanBlock(required=False, default=True)
    sticky_navbar = blocks.BooleanBlock(required=False, default=True)

    # Layout
    padding_y = blocks.CharBlock(required=False, default="1rem")
    padding_x = blocks.CharBlock(required=False, default="2rem")
    font_size = blocks.CharBlock(required=False, default="1rem")
    letter_spacing = blocks.CharBlock(required=False, default="0.5px")
    logo_size = blocks.CharBlock(required=False, default="60px")
    
    # Dimension controls
    width = blocks.CharBlock(required=False, help_text="Navbar width (e.g. 100%, 1200px)")
    height = blocks.CharBlock(required=False, help_text="Navbar height (e.g. 80px)")
    max_width = blocks.CharBlock(required=False, help_text="Maximum width (e.g. 1400px)")
    
    # Styling controls
    border_radius = blocks.CharBlock(required=False, help_text="Border radius (e.g. 5px)")
    border_width = blocks.CharBlock(required=False, default="0px", help_text="Border width (e.g. 1px)")
    border_style = blocks.ChoiceBlock(
        choices=[
            ("solid", "Solid"),
            ("dashed", "Dashed"),
            ("dotted", "Dotted"),
            ("double", "Double"),
            ("none", "None"),
        ],
        default="none",
        required=False
    )
    border_color = blocks.CharBlock(required=False, help_text="Border color (e.g. #000000)")
    margin = blocks.CharBlock(required=False, help_text="Margin (e.g. 0 auto)")

    # Behavior
    scroll_transition = blocks.BooleanBlock(required=False, default=True)
    scroll_threshold = blocks.IntegerBlock(required=False, default=100)
    collapse_on_click = blocks.BooleanBlock(required=False, default=True)
    mobile_breakpoint = blocks.CharBlock(required=False, default="900px")
    hamburger_icon = blocks.CharBlock(required=False, default="fa-solid fa-bars")
    close_icon = blocks.CharBlock(required=False, default="fa-solid fa-xmark")
    dropdown_hover_delay = blocks.FloatBlock(required=False, default=0.2)

    # Animations
    load_animation = blocks.ChoiceBlock(
        choices=[
            ("none", "None"),
            ("fade-in", "Fade In"),
            ("slide-down", "Slide Down"),
            ("zoom", "Zoom In"),
        ],
        default="slide-down",
    )
    animation_duration = blocks.CharBlock(required=False, default="0.5s")
    animation_easing = blocks.CharBlock(required=False, default="ease-in-out")

    # Custom code
    theme = blocks.ChoiceBlock(
        choices=[("classic", "Classic"), ("modern", "Modern"), ("glass", "Glass"), ("gold", "Gold")],
        default="modern",
    )
    custom_css = blocks.TextBlock(required=False)
    custom_js = blocks.TextBlock(required=False)
    ajax_behavior = blocks.TextBlock(required=False)

    def render(self, value, context=None):
        return render_to_string("blocks/navbar_block.html", {"self": value})

