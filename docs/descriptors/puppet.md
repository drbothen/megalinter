---
title: PUPPET linters in MegaLinter
description: puppet-lint is available to analyze PUPPET files in MegaLinter
---
<!-- markdownlint-disable MD003 MD020 MD033 MD041 -->
<!-- @generated by .automation/build.py, please do not update manually -->
<!-- Instead, update descriptor file at https://github.com/oxsecurity/megalinter/tree/main/megalinter/descriptors/puppet.yml -->
# PUPPET

## Linters

| Linter                                                                                     | Additional                                                                                                                                                                             |
|--------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**puppet-lint**](puppet_puppet_lint.md)<br/>[_PUPPET_PUPPET_LINT_](puppet_puppet_lint.md) | [![GitHub stars](https://img.shields.io/github/stars/rodjek/puppet-lint?cacheSeconds=3600)](https://github.com/rodjek/puppet-lint) ![autofix](https://shields.io/badge/-autofix-green) |

## Linted files

- File extensions:
  - `.pp`

## Configuration in MegaLinter

| Variable                    | Description                   | Default value |
|-----------------------------|-------------------------------|---------------|
| PUPPET_FILTER_REGEX_INCLUDE | Custom regex including filter |               |
| PUPPET_FILTER_REGEX_EXCLUDE | Custom regex excluding filter |               |

