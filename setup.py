# ------------------------------------------------------------
# Copyright (c) 2017-present, SeetaTech, Co.,Ltd.
#
# Licensed under the BSD 2-Clause License.
# You should have received a copy of the BSD 2-Clause License
# along with the software. If not, See,
#
#     <https://opensource.org/licenses/BSD-2-Clause>
#
# ------------------------------------------------------------
"""Python setup script."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import os
import shutil
import subprocess
import sys

import setuptools
import setuptools.command.build_py
import setuptools.command.install


def parse_args():
    """Parse arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', default=None)
    args, unknown = parser.parse_known_args()
    args.git_version = None
    args.long_description = ''
    sys.argv = [sys.argv[0]] + unknown
    if args.version is None and os.path.exists('version.txt'):
        with open('version.txt', 'r') as f:
            args.version = f.read().strip()
    if os.path.exists('.git'):
        try:
            git_version = subprocess.check_output(
                ['git', 'rev-parse', 'HEAD'], cwd='./')
            args.git_version = git_version.decode('ascii').strip()
        except (OSError, subprocess.CalledProcessError):
            pass
    if os.path.exists('README.md'):
        with open(os.path.join('README.md'), encoding='utf-8') as f:
            args.long_description = f.read()
    return args


def clean_builds():
    """Clean the builds."""
    for path in ['build', 'sphinx_seeta_theme.egg-info']:
        if os.path.exists(path):
            shutil.rmtree(path)
    if os.path.exists('sphinx_seeta_theme/version.py'):
        os.remove('sphinx_seeta_theme/version.py')


def find_packages(top):
    """Return the python sources installed to package."""
    packages = []
    for root, _, _ in os.walk(top):
        if os.path.exists(os.path.join(root, '__init__.py')):
            packages.append(root)
    return packages


class BuildPyCommand(setuptools.command.build_py.build_py):
    """Enhanced 'build_py' command."""

    def build_packages(self):
        with open('sphinx_seeta_theme/version.py', 'w') as f:
            f.write("from __future__ import absolute_import\n"
                    "from __future__ import division\n"
                    "from __future__ import print_function\n\n"
                    "version = '{}'\n"
                    "git_version = '{}'\n".format(args.version, args.git_version))
        self.packages = find_packages('sphinx_seeta_theme')
        super(BuildPyCommand, self).build_packages()

    def build_package_data(self):
        self.package_data = {'sphinx_seeta_theme': [
            'theme.conf',
            '*.html',
            'static/pygments.css',
            'static/css/*.css',
            'static/js/*.js',
            'static/fonts/font-awesome/css/*.*',
            'static/fonts/font-awesome/fonts/*.*',
            'static/fonts/font-en/css/*.*',
            'static/fonts/font-en/fonts/*.*',
        ]}
        super(BuildPyCommand, self).build_package_data()


class InstallCommand(setuptools.command.install.install):
    """Enhanced 'install' command."""

    def initialize_options(self):
        super(InstallCommand, self).initialize_options()
        self.old_and_unmanageable = True


args = parse_args()
setuptools.setup(
    name='sphinx-seeta-theme',
    version=args.version,
    author='SeetaTech',
    license='BSD 2-Clause',
    description='Sphinx theme for seeta documentations.',
    long_description=args.long_description,
    long_description_content_type='text/markdown',
    packages=find_packages('sphinx_seeta_theme'),
    cmdclass={'build_py': BuildPyCommand, 'install': InstallCommand},
    # See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
    entry_points={'sphinx.html_themes': ['seeta = sphinx_seeta_theme']},
    install_requires=['sphinx>=3.3.0',
                      'commonmark',
                      'sphinxcontrib-katex',
                      'breathe'],
    classifiers=['Framework :: Sphinx',
                 'Framework :: Sphinx :: Theme',
                 'Development Status :: 5 - Production/Stable',
                 'License :: OSI Approved :: MIT License',
                 'Environment :: Console',
                 'Environment :: Web Environment',
                 'Intended Audience :: Developers',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3 :: Only',
                 'Operating System :: OS Independent',
                 'Topic :: Documentation',
                 'Topic :: Software Development :: Documentation'],
)
clean_builds()
