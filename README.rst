Django-Jinja-Markdown
=====================

.. image:: https://github.com/mozmeao/django-jinja-markdown/actions/workflows/ci.yaml/badge.svg
    :target: https://github.com/mozmeao/django-jinja-markdown/actions/workflows/ci.yaml

.. image:: https://img.shields.io/pypi/v/django-jinja-markdown.svg?maxAge=2592000
    :target: https://pypi.python.org/pypi/django-jinja-markdown

`Django-Jinja <http://niwinz.github.io/django-jinja/latest/>`__
(`Jinja2 <http://jinja.pocoo.org/>`__) extension and filter to parse
markdown text in templates.

Requirements
------------

-  `Django <https://www.djangoproject.com/>`__ 3.2+
-  `Django-Jinja <http://niwinz.github.io/django-jinja/latest/>`__
-  `Python-Markdown <https://pythonhosted.org/Markdown/>`__

Installation
------------

Install django-jinja-markdown:

.. code:: shell

    pip install django-jinja-markdown

Add ``django_jinja_markdown`` to ``INSTALLED_APPS``.

To be able to use the ``{% markdown %}`` tag you should add the Jinja extension
to your ``django_jinja`` TEMPLATES extensions list:

.. code:: python

    TEMPLATES = [
        {
            'BACKEND': 'django_jinja.backend.Jinja2',
            'OPTIONS': {
                'extensions': [
                    'django_jinja_markdown.extensions.MarkdownExtension',
                ],
            }
        },
    ]

Basic Use
---------

Examples of using filter in template:

.. code:: jinja

    {{ content|markdown }}
    {{ markdown('this is **bold**') }}

Or with additional settings:

.. code:: jinja

    {{ content|markdown(extensions=['nl2br',]) }}
    {{ markdown(content, extensions=['nl2br',]) }}

Example of using extension:

.. code:: jinja

    {% markdown %}
    Text which will get converted with Markdown.
    {% endmarkdown %}

License
-------

This software is licensed under The MIT License (MIT). For more
information, read the file LICENSE.

History
-------

Forked in 2016 from the
`jingo-markdown <https://github.com/nrsimha/jingo-markdown>`__ project.
Please see CHANGELOG for more history.


Releasing
---------

1. Update the version number in ``django_jinja_markdown/__about__.py``.
2. Add an entry to the change log in the README file.
3. Tag the commit where you changed the above with the version number: e.g. ``1.21``.
4. Push the commit and tag to the github repo.
5. Create a new GitHub release, selecting the tag you just pushed to specify the commit. Hit Publish.
6. Github will build and release the package to PyPI. Monitor the progress via the Actions tab.
