# Project-Creator

[![Build](https://github.com/AidanInceer/ProjectCreator/actions/workflows/build.yml/badge.svg)](https://github.com/AidanInceer/ProjectCreator/actions/workflows/build.yml)
[![Lint](https://github.com/AidanInceer/ProjectCreator/actions/workflows/lint.yml/badge.svg)](https://github.com/AidanInceer/ProjectCreator/actions/workflows/lint.yml)
[![Test](https://github.com/AidanInceer/ProjectCreator/actions/workflows/test.yml/badge.svg)](https://github.com/AidanInceer/ProjectCreator/actions/workflows/test.yml)
[![Scan](https://github.com/AidanInceer/ProjectCreator/actions/workflows/scan.yml/badge.svg)](https://github.com/AidanInceer/ProjectCreator/actions/workflows/scan.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=AidanInceer_BetterChess&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=AidanInceer_BetterChess)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=AidanInceer_BetterChess&metric=coverage)](https://sonarcloud.io/summary/new_code?id=AidanInceer_BetterChess)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=AidanInceer_BetterChess&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=AidanInceer_BetterChess)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=AidanInceer_BetterChess&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=AidanInceer_BetterChess)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=AidanInceer_BetterChess&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=AidanInceer_BetterChess)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=AidanInceer_BetterChess&metric=bugs)](https://sonarcloud.io/summary/new_code?id=AidanInceer_BetterChess)

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
