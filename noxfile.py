import pathlib

import nox

ROOT = pathlib.Path(__file__).parent
nox.options.sessions = ["lint", "lock", "test"]


@nox.session
def test(session: nox.Session) -> None:
    """Run the notebooks."""
    args = [
        "pytest",
        ".",
        "--nbmake",
        "--nbmake-kernel=python3",
        "--nbmake-timeout=3000",
        "-n",
        "auto",
        "-vvv",
    ] + session.posargs

    session.install("git+https://github.com/mcflugen/nbmake.git@mcflugen/add-markers")
    session.install("pytest", "pytest-xdist", "-r", "requirements.in")

    session.run(*args)


@nox.session
def lint(session: nox.Session) -> None:
    """Look for lint."""
    session.install("pre-commit")
    session.run("pre-commit", "run", "--all-files")


@nox.session(python=False)
def install_api_key(session: nox.Session):
    key_file = ROOT / ".opentopography.txt"

    topo_key = input("Enter Your OpenTopography API Key: ")

    with open(key_file, "w") as fp:
        fp.write(topo_key)

    print(f"OpenTopography API Key file is created at {key_file!s}.")


@nox.session
def lock(session: nox.Session) -> None:
    """Create lock files."""
    session.install("pip-tools")

    with open("requirements.txt", "wb") as fp:
        session.run(
            "pip-compile",
            "--resolver=backtracking",
            "--upgrade",
            "requirements.in",
            stdout=fp,
        )
