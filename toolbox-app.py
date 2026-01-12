#!/bin/python3

import os
import sys

def main():
    if len(sys.argv) < 3:
        print("Usage: toolbox-app <container> <absolute-app-path> [args...]")
        sys.exit(1)

    container = sys.argv[1]
    app_path = sys.argv[2]
    args = sys.argv[3:]

    env = os.environ.copy()
    env["DISPLAY"] = env.get("DISPLAY", ":0")
    env["WAYLAND_DISPLAY"] = env.get("WAYLAND_DISPLAY", "wayland-0")
    env["XDG_RUNTIME_DIR"] = env.get("XDG_RUNTIME_DIR", f"/run/user/{os.getuid()}")

    os.execvpe("/usr/bin/toolbox",
               ["/usr/bin/toolbox", "run", "-c", container, app_path, *args],
               env)

if __name__ == "__main__":
    main()