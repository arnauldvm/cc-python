How to build this project
=========================

Introduction
------------

A project MUST provide:

- a folder name convention for build artifacts
- a folder structure for the above-mentioned build artifacts folder
- a list of targets
- > ✂ ✏️ a file called `bin/build.{target}.{ext}` to target each of the build targets ✂
- a build pipeline given the above pretext

Build Folder Name
-----------------

The canonical folder for builds SHALL be named _{`build`}_ and be located at the root of the project repository.
Each project MUST `git ignore` the _{`build`}_ folder.

> ✂ ℹ️ The name of the build folder may depend on the technology used. Other examples: `target`, `tgt`... ✂

Build Folder Structure
----------------------

> ✂  
> ✏️ Example:
>
> Files and folder names MUST be lowercase.
> The result of the build process should create a folder structure as follows:
>
> ```text
> .
> └── build
>     └── {target}
>         └── {project-name}.{ext}
> ```
>
> Below is an example:
>
> ```text
> .
> └── build
>     └── windows
>         └── my-build.exe
> ```
>
> ✂

Build Targets
-------------

> ✂  
> ✏️ Example:
>
> Below is a list of suggested targets for a project
>
> 1. windows
> 2. linux
> 3. macos
>
> ✂

Build script
------------

> ✂  
> ✏️ Example:
>
> Each release target MUST have a `bin/build.{target}.{ext}` file.
>
> The result of this is that every project MUST produce a build for each target
> when the following command is invoked:
>
> ```shell
> bin/build.{target}.{ext}
> ```
>
> The file MUST be placed in the project's `bin` directory.  
> ✂

Build Pipeline
--------------

### Building targets

> ✂  
> ✏️ Example:
>
> `bin/build.{target}.{ext}` should create builds for each of the targets,
> and place the build artifacts in a folder structure outlined above.
>
> ### Linux
>
> ```shell
> bin/build.linux.sh
> ```
>
> ✂
