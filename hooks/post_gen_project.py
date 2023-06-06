#!/usr/bin/env python
from os import linesep
from sys import version_info
import jinja2 as j2

print('# Post hook')

print("- Injecting complex variables in templates (second pass)...")

python_version = f"{version_info.major}.{version_info.minor}"
context = {'postprocess': {
    'python_version': python_version,
}}

j2_loader = j2.FileSystemLoader('.')
j2_env = j2.Environment(loader=j2_loader)
for file in ['pyproject.toml']:
    j2_env.get_template(file).stream(context).dump(file)

if '{{cookiecutter.with_venv}}' == 'yes':
    venv_dir = f".venv{python_version}"
    print(f"- Creating venv '{venv_dir}'...")
    import venv
    venv.EnvBuilder(symlinks=True, with_pip=True).create(venv_dir)
    print('- Upgrading build tools in venv...')
    from subprocess import run
    run([f"{venv_dir}/bin/pip", "install", "--upgrade", "pip", "setuptools"], check=True)

if '{{cookiecutter.with_git}}' == 'yes':
    print('- Initializing git repo...')
    from subprocess import run
    run(["git", "init", "."], check=True)
    if '{{cookiecutter.with_commit}}' == 'yes':
        print('- Creating first commits...')
        run(['git', 'commit', '--allow-empty', '-m', 'Initial commit'], check=True)
        run(['git', 'add', '.'], check=True)
        run(['git', 'commit', '-m', 'Cookiecutter scaffolding with MW Python template'], check=True)
        run(['git', 'tag', 'version/0.0.0'], check=True)


if '{{cookiecutter.with_venv}}' == 'yes':
    print('',
          '! Remember to activate your venv in each shell as follows:',
          f"    $ cd {{cookiecutter.project_slug}}; source {venv_dir}/bin/activate", sep=linesep)
    print('! Remember to initialize your dev install as follows:',
          '    $ pip install -e .[dev]',
          '  and repeat each time you add a dependency', sep=linesep)
