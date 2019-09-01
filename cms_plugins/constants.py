from django.utils.translation import ugettext_lazy as _

BACKGROUND_CHOICES = (
    ('bg-white', _('White'),),
    ('bg-primary', _('Primary'),),
    ('bg-secondary', _('Secondary'),),
    ('bg-info', _('Info'),),
    ('bg-light', _('Light'),),
    ('bg-dark', _('Dark'),),
    ('bg-success', _('Success'),),
    ('bg-danger', _('Danger'),),
    ('bg-transparent', _('Transparent'),),
)

TEXT_COLOR_CHOICES = (
    ('text-white', _('White'),),
    ('text-black', _('Black'),),
    ('text-primary', _('Primary'),),
    ('text-secondary', _('Secondary'),),
    ('text-info', _('Info'),),
    ('text-light', _('Light'),),
    ('text-dark', _('Dark'),),
    ('text-success', _('Success'),),
    ('text-danger', _('Danger'),),
    ('text-muted', _('Muted'),),
)

TEXT_ALIGNMENT_CHOICES = (
    ('text-left-top', _('Left Top'),),
    ('text-center', _('Center'),),
    ('text-left-bottom', _('Left Bottom'),),
)

TEXT_WRAP_CHOICES = (
    ('text-wrap', _('Wrap'),),
    ('text-nowrap', _('No wrap'),),
)

WIDTH_CHOICES = (
    ('full-width', _('Full-Width No Side Margins'),),
    ('container-fluid', _('Full-Width Small Side Margin'),),
    ('container', _('Full-Width Wide Side Margin'),),
    ('wide-centered', _('Wide Centered'),),
    ('col-sm', _('Responsive Column'),),
)
