from jinja2 import Environment, FileSystemLoader
import inspect
import os

def render(view_file, directory = None, **kwargs):
    if directory is None:
        frm = inspect.stack()[1]
        mod = inspect.getmodule(frm[0])
        directory = os.path.dirname(mod.__file__)
    return Environment(loader=FileSystemLoader(directory)).get_template(view_file).render(**kwargs)
