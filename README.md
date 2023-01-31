# Project-Creator

[![Build](https://github.com/AidanInceer/ProjectCreator/actions/workflows/build.yml/badge.svg)](https://github.com/AidanInceer/ProjectCreator/actions/workflows/build.yml)
[![Lint](https://github.com/AidanInceer/ProjectCreator/actions/workflows/lint.yml/badge.svg)](https://github.com/AidanInceer/ProjectCreator/actions/workflows/lint.yml)
[![Test](https://github.com/AidanInceer/ProjectCreator/actions/workflows/test.yml/badge.svg)](https://github.com/AidanInceer/ProjectCreator/actions/workflows/test.yml)
[![Scan](https://github.com/AidanInceer/ProjectCreator/actions/workflows/scan.yml/badge.svg)](https://github.com/AidanInceer/ProjectCreator/actions/workflows/scan.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Introduction

Sets up a project directory based on pre-defined project types, git and cloud providers.

## Getting Started

Download the repo.

## Usage

Run main.py with the required parameters:

```
-h, --help           show this help message and exit
-n , --projectname   Sets the root folder name of the project.
-p , --projectpath   Sets Absolute path of project. e.g. 'c:/Users/projects'.
-t , --projecttype   Sets the project type, choose from the following options: 'default', 'flask'.
-g , --gitprovider   Sets the git provider for the project, choose from the following options: 'github', 'gitlab', 'ADO','bitbucket', 'none'.
-c , --cloudtype     Sets the cloud provider for the project, choose from the following options: 'aws', 'gcp','azure', 'none'.
```
