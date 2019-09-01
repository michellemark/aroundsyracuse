import os
import boto3
import logging

from cms import constants


def get_ssm_parameter(parameter_name):
    parameter_value = None

    try:
        ssm_parameter = ssm.get_parameter(Name=parameter_name, WithDecryption=True)
    except:
        logger.error(f"SSM parameter not found : {parameter_name}")
    else:
        parameter_value = ssm_parameter["Parameter"]["Value"]

    return parameter_value


logger = logging.getLogger(__name__)
SETTINGS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.join(SETTINGS_DIR, '..')
ssm_db_engine = None
ssm_db_name = None
ssm_db_user = None
ssm_db_password = None
ssm_db_host = None
ssm_db_port = None

if os.environ.get("DJANGO_SETTINGS_MODULE") == "aroundsyracuse.settings.prod":
    session = boto3.Session(region_name="us-east-1")
    ssm = session.client("ssm")
    SECRET_KEY = get_ssm_parameter("/AroundSyracuse/Prod/SECRET_KEY")
    DEFAULT_FROM_EMAIL = get_ssm_parameter("/AroundSyracuse/Prod/DEFAULT_FROM_EMAIL")
    SERVER_EMAIL = DEFAULT_FROM_EMAIL
    ssm_site_admin_name = get_ssm_parameter("/AroundSyracuse/SiteAdmin/Name")
    ssm_site_admin_email = get_ssm_parameter("/AroundSyracuse/SiteAdmin/Email")
    ADMINS = [(ssm_site_admin_name, ssm_site_admin_email)]
    ssm_db_engine = get_ssm_parameter("/AroundSyracuse/Prod/DB_ENGINE")
    ssm_db_name = get_ssm_parameter("/AroundSyracuse/Prod/DB_NAME")
    ssm_db_user = get_ssm_parameter("/AroundSyracuse/Prod/DB_USERNAME")
    ssm_db_password = get_ssm_parameter("/AroundSyracuse/Prod/DB_PASSWORD")
    ssm_db_host = get_ssm_parameter("/AroundSyracuse/Prod/DB_HOSTNAME")
    ssm_db_port = get_ssm_parameter("/AroundSyracuse/Prod/DB_PORT")
    STATIC_ROOT = get_ssm_parameter("/AroundSyracuse/Prod/STATIC_ROOT")
    MEDIA_ROOT = get_ssm_parameter("/AroundSyracuse/Prod/MEDIA_ROOT")
    RECAPTCHA_PRIVATE_KEY = get_ssm_parameter("/AroundSyracuse/Prod/RECAPTCHA_PRIVATE_KEY")
    RECAPTCHA_PUBLIC_KEY = get_ssm_parameter("/AroundSyracuse/Prod/RECAPTCHA_PUBLIC_KEY")

DEBUG = False
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
APPEND_SLASH = True
ALLOWED_HOSTS = [".aroundsyracuserealty.com"]
SITE_ID = 2
INSTALLED_APPS = [
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'cms',
    'menus',
    'treebeard',
    'sekizai',
    'filer',
    'easy_thumbnails',
    'mptt',
    'djangocms_text_ckeditor',
    'djangocms_icon',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_bootstrap4',
    'djangocms_bootstrap4.contrib.bootstrap4_alerts',
    'djangocms_bootstrap4.contrib.bootstrap4_badge',
    'djangocms_bootstrap4.contrib.bootstrap4_card',
    'djangocms_bootstrap4.contrib.bootstrap4_carousel',
    'djangocms_bootstrap4.contrib.bootstrap4_collapse',
    'djangocms_bootstrap4.contrib.bootstrap4_content',
    'djangocms_bootstrap4.contrib.bootstrap4_grid',
    'djangocms_bootstrap4.contrib.bootstrap4_jumbotron',
    'djangocms_bootstrap4.contrib.bootstrap4_link',
    'djangocms_bootstrap4.contrib.bootstrap4_listgroup',
    'djangocms_bootstrap4.contrib.bootstrap4_media',
    'djangocms_bootstrap4.contrib.bootstrap4_picture',
    'djangocms_bootstrap4.contrib.bootstrap4_tabs',
    'djangocms_bootstrap4.contrib.bootstrap4_utilities',
    'djangocms_video',
    'aldryn_apphooks_config',
    'aldryn_categories',
    'aldryn_common',
    'aldryn_newsblog',
    'aldryn_people',
    'aldryn_translation_tools',
    'parler',
    'sortedm2m',
    'taggit',
    'djangocms_googlemap',
    'cms_plugins',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
]
ROOT_URLCONF = 'aroundsyracuse.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
            ],
        },
    },
]
WSGI_APPLICATION = 'aroundsyracuse.wsgi.application'

if ssm_db_engine and ssm_db_name and ssm_db_user and ssm_db_password and ssm_db_host and ssm_db_port:
    DATABASES = {
        'default': {
            'ENGINE': ssm_db_engine,
            'NAME': ssm_db_name,
            'USER': ssm_db_user,
            'PASSWORD': ssm_db_password,
            'HOST': ssm_db_host,
            'PORT': ssm_db_port,
            'CONN_MAX_AGE': 600,
        }
    }
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
LANGUAGE_CODE = 'en'
LANGUAGES = [
    (LANGUAGE_CODE, 'English'),
    ('fr', 'French'),
    ('es', 'Spanish')
]
CMS_LANGUAGES = {
    1: [
        {
            'code': 'en',
            'name': 'English',
            'public': True,
        },
        {
            'code': 'es',
            'name': 'Spanish',
            'fallbacks': ['en', 'fr'],
            'public': True,
            'hide_untranslated': True,
            'redirect_on_fallback': True,
        },
        {
            'code': 'fr',
            'name': 'French',
            'fallbacks': ['en', 'es'],
            'public': True,
            'hide_untranslated': True,
            'redirect_on_fallback': True,
        },
    ]
}
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'detailed': {
            'format': '%(asctime)s %(levelname)s [%(name)s: %(pathname)s %(funcName)s line:%(lineno)s] -- %(message)s',
            'datefmt': '%m-%d-%Y %H:%M:%S'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'formatter': 'detailed',
            'class': 'django.utils.log.AdminEmailHandler',
        },
    },
    'loggers': {
        'django.request': {
            'level': 'ERROR',
            'handlers': ['mail_admins'],
            'propagate': True,
        },
    }
}
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_URL = '/static/'
MEDIA_URL = "/media/"
FIXTURE_DIRS = [
    os.path.join(BASE_DIR, "fixtures"),
]
CMS_PERMISSION = True
CMS_TOOLBAR_ANONYMOUS_ON = False
CMS_DEFAULT_X_FRAME_OPTIONS = constants.X_FRAME_OPTIONS_SAMEORIGIN
CMS_TEMPLATES = [
    ('fullwidth.html', 'Fullwidth'),
    ('fullwidth-narrow-margins.html', 'Fullwidth Narrow Margins'),
    ('sidebar-left.html', 'Sidebar Left'),
    ('sidebar-right.html', 'Sidebar Right'),
    ('home.html', 'Home page template'),
    ('template_blog.html', 'Blog Template'),
]
CMS_PAGE_WIZARD_DEFAULT_TEMPLATE = "fullwidth.html"
CMS_PAGE_WIZARD_CONTENT_PLACEHOLDER = "content"
CMS_PLACEHOLDER_CONF = {
    'home_featured_article': {
        'name': 'Home Featured Article',
        'plugins': ['NewsBlogFeaturedArticlesPlugin', 'Bootstrap4PicturePlugin', 'TextPlugin']
    },
    'banner_image': {
        'plugins': ['Bootstrap4PicturePlugin', ]
    }
}
THUMBNAIL_HIGH_RESOLUTION = True
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
FILER_CANONICAL_URL = 'sharing/'
DJANGOCMS_BOOTSTRAP4_TAG_CHOICES = ['div', 'section', 'article', 'header', 'footer', 'aside']
DJANGOCMS_BOOTSTRAP4_GRID_SIZE = 12
DJANGOCMS_BOOTSTRAP4_GRID_CONTAINERS = (
    ('container', 'Container'),
    ('container-fluid', 'Fluid container'),
)
DJANGOCMS_BOOTSTRAP4_GRID_COLUMN_CHOICES = (
    ('col', 'Column'),
)
DJANGOCMS_BOOTSTRAP4_USE_ICONS = True
DJANGOCMS_BOOTSTRAP4_CAROUSEL_TEMPLATES = (
    ('default', 'Default'),
)
DJANGOCMS_BOOTSTRAP4_TAB_TEMPLATES = (
    ('default', 'Default'),
)
DJANGOCMS_BOOTSTRAP4_SPACER_SIZES = (
    ('0', '* 0'),
    ('1', '* .25'),
    ('2', '* .5'),
    ('3', '* 1'),
    ('4', '* 1.5'),
    ('5', '* 3'),
)
DJANGOCMS_BOOTSTRAP4_CAROUSEL_ASPECT_RATIOS = (
    (16, 9),
    (4, 3),
    (19, 6),
    (1, 1),
)
DJANGOCMS_BOOTSTRAP4_COLOR_STYLE_CHOICES = (
    ('primary', 'Primary'),
    ('secondary', 'Secondary'),
    ('success', 'Success'),
    ('danger', 'Danger'),
    ('warning', 'Warning'),
    ('info', 'Info'),
    ('light', 'Light'),
    ('dark', 'Dark'),
    ('custom', 'Custom'),
)
DJANGOCMS_VIDEO_ALLOWED_EXTENSIONS = ['mp4', 'webm', 'ogv']
DJANGOCMS_VIDEO_TEMPLATES = [
    ('responsive', 'Responsive'),
]
DJANGOCMS_PICTURE_NESTING = True
DJANGOCMS_PICTURE_RESPONSIVE_IMAGES = True
DJANGOCMS_PICTURE_TEMPLATES = [
    ('fullwidth', 'Full-Width'),
    ('match_height', 'Match Height'),
    ('overlay_caption', 'Overlay Caption'),
    ('display-desktop', 'Display Desktop/Tablet Only'),
    ('display-mobile', 'Display Mobile Only'),
    ('default', 'Default'),
    ('inline', 'Inline'),
]
DJANGOCMS_PICTURE_ALIGN = [
    ('top', 'Top Aligned'),
    ('middle', 'Middle Aligned'),
    ('bottom', 'Bottom Aligned'),
    ('text-top', 'Text Top Aligned'),
    ('text-bottom', 'Text Bottom Aligned'),
]
CMSPLUGIN_FILER_IMAGE_STYLE_CHOICES = (
    ('default', 'Default'),
    ('fullwidth', 'Full-Width'),
    ('display-desktop', 'Display Desktop/Tablet Only'),
    ('display-mobile', 'Display Mobile Only'),
    ('match_height', 'Match Height'),
    ('tile_overlay', 'Caption Overlay'),
    ('inline', 'Inline'),
)
CKEDITOR_SETTINGS = {
    'language': '{{ language }}',
    'toolbar': 'CMS',
    'stylesSet': 'default:/static/js/addons/ckeditor.wysiwyg.js'
}
