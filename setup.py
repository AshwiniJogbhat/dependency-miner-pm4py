import pathlib
from setuptools import setup

CURRENT_PATH = pathlib.Path(__file__).parent

README = (CURRENT_PATH/"README.md").read_text()

setup(
    name="dependency-miner-pm4py",
    version="1.0.1",
    description="It mines long-term dependencies between events and results into a Precise model",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/AshwiniJogbhat/dependency-miner-pm4py",
    author="Ashwini Jogbhat",
    author_email="ashwini.jogbhat@rwth-aachen.de",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["dependency-miner"],
    include_package_data=True,
    install_requires=['numpy', 'pm4py',
    ],
    entry_points={
        "console_scripts": [
            "miner=dependency-miner.ltminer:main",
        ]
    },
)