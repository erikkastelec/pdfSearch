import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    install_requires=[
        "camelot-py==0.8.2",
        "certifi==2020.6.20",
        "cffi==1.14.2",
        "chardet==3.0.4; python_version > '3.0'",
        "click==7.1.2",
        "cryptography==3.1",
        "cycler==0.10.0",
        "decorator==4.4.2",
        "distro==1.5.0",
        "et-xmlfile==1.0.1",
        "fuzzywuzzy==0.18.0",
        "imageio==2.9.0",
        "iso-639==0.4.5",
        "jdcal==1.4.1",
        "kiwisolver==1.2.0",
        "langdetect==1.0.8",
        "matplotlib==3.3.1",
        "memory-profiler==0.57.0",
        "networkx==2.5",
        "numpy==1.19.2",
        "opencv-python==4.3.0.36",
        "openpyxl==3.0.5",
        "pandas==1.1.2",
        "pdf2image==1.14.0",
        "pdfminer-six==20200726",
        "pdfminer.six==20200726",
        "pillow==7.2.0",
        "psutil==5.7.2",
        "pycparser==2.20",
        "pyparsing==2.4.7",
        "pypdf2==1.26.0",
        "pytesseract==0.3.4",
        "python-dateutil==2.8.1",
        "python-levenshtein==0.12.0",
        "pytz==2020.1",
        "pywavelets==1.1.1",
        "scikit-image==0.17.2",
        "scipy==1.5.2",
        "six==1.15.0",
        "sortedcontainers==2.2.2",
        "tabula-py==2.2.0",
        "tifffile==2020.9.3",
        "wand==0.6.2",
        "yattag==1.14.0",
    ],
    name="PDFScraper",
    version="1.1.7",
    author="Erik Kastelec",
    author_email="erikkastelec@gmail.com",
    description="PDF text and table search",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/erikkastelec/PDFScraper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
    python_requires=">=3.6",
)
