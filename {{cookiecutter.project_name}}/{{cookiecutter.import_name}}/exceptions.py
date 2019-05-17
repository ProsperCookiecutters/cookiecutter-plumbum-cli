"""custom exceptions for {{cookiecutter.project_name}}"""

class {{ cookiecutter.project_name | replace('-', ' ') | replace('_', ' ') | title | replace(' ', '')}}(Exception):
    """parent exception for {{cookiecutter.project_name}}"""
