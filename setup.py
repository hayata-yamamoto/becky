from typing import NoReturn, IO

from setuptools import find_packages, setup


def main() -> NoReturn:

    f: IO
    with open('requirements.txt', 'r') as f:
        req = f.read().splitlines()

    setup(
        name="becky",
        description="NLP modules",
        version="0.1.0",
        install_requires=req,
        packages=find_packages(exclude=["becky/data"])
    )

if __name__ == '__main__':
    main()
