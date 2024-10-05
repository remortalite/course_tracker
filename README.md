# Course tracker

## Description

Project is used for personal tracking your progress with open courses.
The app can be used for tracking progress,
sharing progress with friends,
making some goals to achieve.

## Technical details

Project written on Python using framework Django.

Steps to achieve:

- MVP
- Version 0.9 (pre-release)
- Version 1.0
- Dockerization
- Deploy at remote server
- Telegram bot

## Development

### Step 1. MVP.

#### 1.1

The app contains minimal user managment and saving some basic info about courses.

Models to realise: `User`, `Course`.

Organize code with Makefile.

Make some basic UI. Translations using *i18n*.

#### 1.2

The courses contain authors and can be private or open. The user can set visibility of a course.

New model: Task.
Contains fields: name, description, link, status

There is a possibility to track progress.

A progress can be visible on the main page.

The Course contains Tasks.
