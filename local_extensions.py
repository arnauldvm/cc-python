from jinja2.ext import Extension

from sys import version_info

class PythonVersionExtension(Extension):
    def __init__(self, environment):
        super(PythonVersionExtension, self).__init__(environment)
        environment.filters['pyversion'] = lambda fmt: fmt.format(version=version_info)
