How to create a new release of this system
==========================================

Introduction
------------

This document is to describe the release pipeline,
which is taking the result of the artifacts created according to [BUILDING.md](BUILDING.md)
and publish a release to the various release targets for the project.

We propose:

- a set of release targets that are allowable
- a pipeline for handling the release folder's artifacts

It is NOT the purpose of this document to describe how a project might create a build,
NOR is it describing a structure in which projects MUST write build artifacts to.
It is describing the structure of the releases themselves.

Release Pipeline
----------------

> ✂  
> ✏️ Example:
>
> ### Create a build from current branch
>
> Process is outlined in [BUILDING.md](BUILDING.md)
>
> 1. Clean the build directory
> 2. run: `bin/build.{target}.{ext}`
>
> ### Bump the version of the project
>
> Projects use [Semantic versioning](https://semver.org/).
>
> ### Generate Changelog
>
> Write changelog in [CHANGELOG.md](CHANGELOG.md).
>
> ### Commit the bump + changelog update
>
> A project MUST generate a commit with the changes.
>
> ### Tag the commit with the bumped version
>
> A project MUST be tagged with [Semantic versioning](https://semver.org/).
>
> ### Sign the releases
>
> - MUST be a pgp signature
> - MUST be the same pgp key as is registered with Github
> - MUST be a detached ascii-armored (.asc) signature
> - All files in the build folder MUST have an associated signature file
>
> ### Push changelog & version bump
>
> ### Run Release Targets
>
> For each of the desired release targets, prepare and push the release.
>
> #### Example Release Targets
>
> 1. Github
> 2. Docker Hub
>
> ✂
