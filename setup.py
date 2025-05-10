from setuptools import setup, find_packages

setup(
    name="Rasa Dependencies",
    version="0.1.0",
    description="Dependencies for a project that requires the same dependencies as Rasa Open Source.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Kevin Turnbull",
    author_email="kevin@kevinturnbull.ca",
    url="https://github.com/kevinturnbull/rasa-dependencies",
    packages=find_packages(),
    install_requires=[ 

    ],
    python_requires="==3.10",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)