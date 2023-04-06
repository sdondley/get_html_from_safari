#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Steve Dondley",
    author_email='s@dondley.com',
    python_requires='>=3.6',
    package_data={"get_html_from_safari": ["applescripts/*"]},
    entry_points={
        'console_scripts': [
            'html-source-get=get_html_from_safari.get_html:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Grabs HTML from Safari browser",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='get_html_from_safari',
    name='get_html_from_safari',
    packages=find_packages(include=['get_html_from_safari', 'get_html_from_safari.*']),
    platforms='MacOS',
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/sdondley/get_html_from_safari',
    version='0.2.4',
    zip_safe=False,
)
