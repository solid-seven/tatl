"""Modules"""
import subprocess
import sys


def execute_ebpf() -> bool:
    """
    Create a subprocess to invoke bootstrap, and time it out after 10s
    """
    results = subprocess.run(
        args=[
            "timeout",
            "10s",
            "$GITHUB_WORKSPACE/libbpf-bootstrap/examples/c/bootstrap " \
            "> $GITHUB_WORKSPACE/ebpf-output.log",
        ],
        shell=True,
        check=False,
    )
    if results.returncode in [0, 124]:
        return True
    return False


if __name__ == "__main__":
    if execute_ebpf():
        sys.exit(0)
    sys.exit(1)
