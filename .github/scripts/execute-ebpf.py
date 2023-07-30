import subprocess
import sys


def execute_ebpf() -> bool:
    results = subprocess.run(
        args=[
            "sudo",
            "timeout",
            "10s",
            "$GITHUB_WORKSPACE/libbpf-bootstrap/examples/c/bootstrap > $GITHUB_WORKSPACE/ebpf-output.log"
        ],
        shell=True
    )
    if results.returncode in [0, 124]:
        return True
    return False

if __name__ == '__main__':
    if execute_ebpf():
        sys.exit(0)
    sys.exit(1)