# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

project_url = 'https://github.com/ociu/sphinx-traceability-extension'

requires = ['Sphinx>=0.6']

setup(
    name='mlx.traceability',
    version='1.3.0',
    url=project_url,
    download_url=project_url + '/archive/v1.3.0.tar.gz',
    license='GNU General Public License v3 (GPLv3)',
    author='Stein Heselmans',
    author_email='teh@melexis.com',
    description='Sphinx traceability extension (Melexis fork)',
    long_description=open("README.rst").read(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(exclude=['tests', 'example']),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
    keywords = ['traceability',
                'requirements engineering',
                'requirements management',
                'software engineering',
                'systems engineering',
                'sphinx',
                'requirements',
                'ASPICE',
                'ISO26262',
                'ASIL'
            ]
)
