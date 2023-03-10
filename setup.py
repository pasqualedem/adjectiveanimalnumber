import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="adjectiveanimalnumber",
    version="0.0.1",
    author="Pasquale De Marinis",
    author_email="pas.demarinis@gmail.com",
    url="https://github.com/pasqualedem/adjectiveanimalnumber",
    description="A simple package to generate random adjectives with an animal name and a random integer.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3',                # Minimum version requirement of the package
    entry_points={
        "console_scripts": [
            "adjectiveanimalnumber=adjectiveanimalnumber.__main__:main",
        ]
    },
)