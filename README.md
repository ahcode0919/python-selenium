# Selenium Automation With Python ![](https://github.com/ahcode0919/python-selenium/actions/workflows/ci.yml/badge.svg?branch=main)

Selenium automation project implemented in Python. Runs a small suite of tests against [Choose a License](https://choosealicense.com)

## Setup

Project supports local development and VSCode Dev container development

### Local Development Installation

Note: Project uses `uv` and `just` to manage project configuration and commands

* Install dependencies via Homebrew - `brew bundle install`
* Sync project - `just sync`

## Project Commands

* Local
  * `just lint` - lint project files
* Dev container
  * `just lint` - lint and stylecheck project files
* Run unit tests: `just test`
* Install dependency: `uv add {package}`
