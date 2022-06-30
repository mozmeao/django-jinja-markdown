DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

INSTALLED_APPS = (
    "django_jinja",
    "django_jinja_markdown",
)

TEMPLATES = [
    {
        "BACKEND": "django_jinja.backend.Jinja2",
        "OPTIONS": {
            "match_extension": None,
            "extensions": [
                "jinja2.ext.do",
                "jinja2.ext.loopcontrols",
                "jinja2.ext.i18n",
                "django_jinja_markdown.extensions.MarkdownExtension",
            ],
        },
    },
]

SECRET_KEY = "unique snowflake"
USE_I18N = False
