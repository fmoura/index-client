from setuptools import setup, find_packages

setup(
    name="index-client",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "aiohttp==3.11.12",
    ],
    entry_points={
        "console_scripts": [
            "index-client=index_client.cli:main",
        ],
    },
)