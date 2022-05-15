from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pinata',
    version='0.0.1',
    description="Unofficial library for accessing Pinata's IPFS APIs",
    py_modules=['pinata'],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",

    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        "requests>=2.0"
    ],
    extras_require={
        'dev':[
            "pytest==7.0",

        ]
    },
    url="https://github.com/GrishonNganga/Pinata-Python",
    author="Grishon Ng'ang'a",
    author_email="grishon.nganga01@gmail.com"

)