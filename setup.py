# -*- coding: utf-8 -*-
"""Installer for the collective.playlist package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst', 'r').read(),
    open('CONTRIBUTORS.rst', 'r').read(),
    open('CHANGES.rst', 'r').read(),
])

setup(
    name='collective.playlist',
    version='1.0b2.dev0',
    description="Audio playlist player for Plone",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Topic :: Multimedia :: Sound/Audio :: Players",
        'Development Status :: 5 - Production/Stable',
        "Environment :: Web Environment",
        "Framework :: Plone :: 5.2",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='audio player playlist Plone',
    author='ksuess',
    author_email='k.suess@rohberg.ch',
    url='https://pypi.python.org/pypi/collective.playlist',
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['collective'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'plone.app.dexterity',
        'plone.api',
        'Products.GenericSetup>=1.8.2',
        'setuptools',
        'z3c.jbot',
    ],
    extras_require={
        'test': [
            'plone.testing>=5.0.0',
            "plone.app.testing [robot]",
            "plone.app.robotframework",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
