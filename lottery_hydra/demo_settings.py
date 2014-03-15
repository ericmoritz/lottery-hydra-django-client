from hydraclient.core.settings import DEFAULT_JSONLD_CONTEXT

INSTALLED_APPS = [
    "hydraclient.contrib.django.hydraclient", 
    "lottery_hydra",
]

TEMPLATE_CONTEXT_PROCESSORS = (
"django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
"django.core.context_processors.static",
"django.core.context_processors.tz",
"django.core.context_processors.request",
"django.contrib.messages.context_processors.messages",
)

APPEND_SLASH = False
ROOT_URLCONF = "lottery_hydra.urls"

DEFAULT_JSONLD_CONTEXT = dict(
    DEFAULT_JSONLD_CONTEXT,
    **{
        "lottery": "http://vocab-ld.org/vocabs/lottery#"
    }
)

DEBUG=True
TEMPLATE_DEBUG=True
