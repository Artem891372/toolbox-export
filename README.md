# toolbox-export (fork)

⚠️ This is a fork of https://github.com/mrvladus/toolbox-export

This fork adds proper display (X11 / Wayland) environment handling
for exported applications by introducing a wrapper launcher.

## Why this fork exists

The original `toolbox-export` generates `.desktop` files that call
`toolbox run -c <container> <app>` directly.

On some systems this does not work correctly for GUI applications,
because required display-related environment variables are missing
(e.g. `DISPLAY`, `WAYLAND_DISPLAY`, `XDG_RUNTIME_DIR`).

This fork introduces an additional launcher script (`toolbox-app.py`)
that:

- preserves the host display context
- supports both X11 and Wayland
- allows passing arbitrary arguments to the application

## About toolbox-export

Script for exporting applications from toolbox or any other containers.

It exports `.desktop` files to `~/.local/share/applications`
and application icons to `~/.local/share/icons`.

## Install

Clone the repository and run install script:

```bash
git clone https://github.com/Artem891372/toolbox-export.git
cd toolbox-export
./install.sh
```
Make sure ~/.local/bin is in your PATH.

## Usage

Enter the container:
```bash
toolbox enter
```
Run command:
```bash
toolbox-export APP
```
For example, to export VSCode:
```bash
toolbox-export code
```
