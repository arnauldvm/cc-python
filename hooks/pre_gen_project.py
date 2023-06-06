#!/usr/bin/env python
import json
import re

print('# Pre hook')

print("- Verifying format of context variables...")

context = json.loads("""
{{cookiecutter | jsonify}}
""")

rules = {
    'project_slug': r'^\S+$',  # avoid spaces
    'author_email': r'^(\S+)@(\S+)\.(\S+)$',
    'dist_name': r'(?i)^([A-Z0-9]|[A-Z0-9][A-Z0-9._-]*[A-Z0-9])$',
    #   PEP-423; PEP508 ^(?i)([A-Z0-9]|[A-Z0-9][A-Z0-9._-]*[A-Z0-9])$
    'pack_name': r'^[a-z][a-z0-9]*$',
    #   PEP8 (lowercase, no '_')
    #   & https://docs.python.org/3/reference/lexical_analysis.html#identifiers
    'cli_cmd_name': r'^\S+$',  # avoid spaces
    'with_venv': r'^(yes|no)$',
    'with_git': r'^(yes|no)$',
    'with_commit': r'^(yes|no)$',
}

for k, r in rules.items():
    if k not in context:
        raise LookupError(f"Missing  context variable '{k}', abort.")
    if not re.match(r, context[k]):
        raise ValueError(f"Invalid context variable {k}={context[k]!r} "
                         f"does not match {r!r}, abort.")


if '{{cookiecutter.with_git}}' == 'yes':
    print("- Making sure git is available...")
    from subprocess import run
    run(["git", "version"], check=True)
