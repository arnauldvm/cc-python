# Pendragon cookiecutter template for Python

## Configuration: Context variables

- `project_name`: Human friendly name of the project
     - _default_: "Test project"
- `project_slug`: Directory name for the project
     - _constraint_: no space
     - _automatically computed from_ `project_name`
     - _default_: "test-project"
- `project_description`: Long description of the project
     - _default_: "This test project aims at demonstrating the use of cookiecutter"
- `author_fullname`: First name and last name of the main author
     - _default_: "Arnauld Van Muysewinkel"
- `author_email`: Email of the main author
     - _constraint_: valid email address
     - _default_: "avm@pendragon.be"
- `dist_name`: Name for publishing the Python package in PyPI repository
     - _constraint_: only letters, digits, ".", "-", "_", starts and ends with letter or digit
     - _automatically computed from_ `project_slug`
     - _default_: "be_pendragon_test_project"
- `package_name`: Name of the Python package
     - _constraint_: lowercase and digits, starts with lowercase
     - _automatically computed from_ `project_slug`
     - _default_: "testproject"
- `cli_cmd_name`: Name of the CLI command
     - _constraint_: no space
     - _automatically computed from_ `package_name`
     - _default_: "testproject"
- `with_venv`: Activate creation of Python venv
     - _constraint_: "yes" or "no"
     - _default_: "yes"
- `with_git`: Activate creation of git repo
     - _constraint_: "yes" or "no"
     - _default_: "yes"
- `with_commit`: Create first git commits
     - _constraint_: "yes" or "no"
     - ignored unless `with_git=yes`
     - _default_: "yes"

## Structure of generated project

- `{{....project_slug}}/`:
   - `.gitignore`
   - `.git/` _(only if `{{...with_git}}` == "yes")
   - `.venv/` _(only if `{{...with_venv}}` == "yes")
   - `pyproject.toml`
   - `src/`
      - `{{....package_name}}/`
         - `__init__.py`
         - `cli.py` # Sample CLI providing access to token module
         - `token.py`  # Sample module providing token generation features

   - `BUILDING.md`
   - `CHANGELOG.md`
   - `CONTRIBUTING.md`
   - `INSTALLATION.md`
   - `README.md`
   - `RELEASING.md`
   - `ROADMAP.md`
   - `TESTING.md`
   - `USAGE.md`
