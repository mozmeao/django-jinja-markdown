Django-Jinja-Markdown
=====================

.. image:: https://github.com/mozmeao/django-jinja-markdown/actions/workflows/ci.yaml/badge.svg
    :target: https://github.com/mozmeao/django-jinja-markdown/actions/workflows/ci.yaml

.. image:: https://img.shields.io/pypi/v/django-jinja-markdown.svg
    :target: https://pypi.org/project/django-jinja-markdown/

`Django-Jinja <http://niwinz.github.io/django-jinja/latest/>`__
(`Jinja2 <https://palletsprojects.com/projects/jinja>`__) extension and filter to parse markdown text in templates.

Requirements
------------

-  `Django <https://www.djangoproject.com/>`__
-  `Django-Jinja <https://pypi.org/project/django-jinja/>`__
-  `Python-Markdown <https://pypi.org/project/Markdown/>`__

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

1. Update the version number in ``pyproject.toml``.
2. Add an entry to the CHANGELOG file.
3. Tag the commit with the version number: e.g. ``1.21``.
4. Push the commit and tag to the github repo.
5. Create a new GitHub release, selecting the tag you just pushed to specify the commit. Hit Publish.
6. Github will build and release the package to PyPI. Monitor the progress via the Actions tab.
