from django_jinja import library
from markdown import markdown as _markdown
from markupsafe import Markup


@library.filter
@library.global_function
def markdown(text, *args, **kwargs):
    """
    Parse text with markdown library.

    :param text:   - text for parsing;
    :param args:   - markdown arguments (http://freewisdom.org/projects/python-markdown/Using_as_a_Module);
    :param kwargs: - markdown keyword arguments (http://freewisdom.org/projects/python-markdown/Using_as_a_Module);
    :return:       - parsed result.
    """
    return Markup(_markdown(text, *args, **kwargs))
