#! /usr/bin/env python3
from importlib import metadata


def get_package_version(pkg_name: str) -> tuple[bool, str]:
    try:
        version = metadata.version(pkg_name)
        return True, version
    except metadata.PackageNotFoundError:
        return False, "Not found"


def validate_required_packages(
        pkg_list: dict[str, str]) -> tuple[bool, list[str]]:
    missing: list[str] = []
    for pkg_name, description in pkg_list.items():
        found, version = get_package_version(pkg_name)
        if found:
            print(f"[OK] {pkg_name} ({version}) - {description}")
        else:
            print(f"[MISSING] {pkg_name}")
            missing.append(pkg_name)
    return len(missing) == 0, missing


def print_install_help(missing_pkgs: list[str]) -> None:
    pkgs = ", ".join(missing_pkgs)
    print(f"\nMissing packages: {pkgs}")
    print("\nInstallation instructions:")
    print(" pip    : pip install -r requirements.txt")
    print(" Poetry : poetry install && poetry run python loading.py")


def print_comparison_pip_poetry() -> None:
    print("\nDependency Management Comparison:")
    print("pip:\n Uses requirements.txt to list dependencies.")
    print(" Does not generate a lock file.")
    print(" Requires manual environment activation")
    print("Poetry:\n \
Uses pyproject.toml to define project metadata and dependencies.")
    print(" Generates a poetry.lock file.")


def generate_matrix_signal(
    size: int = 1000
) -> None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")
    print(f"Processing {size} data points...")

    data = np.random.normal(loc=50, scale=15, size=size)
    df = pd.DataFrame({"Value": data})

    print("Generating visualization...")
    fig, axis = plt.subplots(figsize=(8, 5))
    axis.hist(
        df["Value"],
        bins=30,
        color="blue",
        edgecolor="black",
        alpha=0.7,
    )

    axis.set_title("Matrix Analysis")
    axis.set_xlabel("Time")
    axis.set_ylabel("Signal")
    axis.grid(True, alpha=0.3)

    plt.tight_layout()
    output_file = "matrix_analysis.png"
    plt.savefig(output_file)
    plt.close(fig)

    print("\nAnalysis complete!")
    print(f"Results saved to: {output_file}")


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    packages: dict[str, str] = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready",
    }
    print("Checking dependencies:")
    found, missing = validate_required_packages(packages)
    if found:
        generate_matrix_signal()
    else:
        print_install_help(missing)
        print_comparison_pip_poetry()


if __name__ == "__main__":
    main()
