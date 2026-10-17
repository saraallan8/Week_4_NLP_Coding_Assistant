import subprocess


def run_code(code):
    try:
        result = subprocess.run(
            [
                "docker", "run",
                "--rm",
                "--network", "none",
                "--memory", "128m",
                "--cpus", "0.5",
                "--pids-limit", "64",
                "--read-only",
                "--tmpfs", "/tmp:rw,noexec,nosuid,size=16m",
                "--user", "10001:10001",
                "python:3.12-alpine",
                "python", "-c", code
            ],
            capture_output=True,
            text=True,
            timeout=30
        )

        return result.stdout, result.stderr

    except subprocess.TimeoutExpired:
        return "", "Execution timed out."

    except FileNotFoundError:
        return "", "Docker was not found. Make sure Docker Desktop is running."