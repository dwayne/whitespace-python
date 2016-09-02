import re

from codecs import open

from setuptools import find_packages, setup


with open('whitespace/__init__.py', 'r', 'utf-8') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        f.read(), re.MULTILINE).group(1)


with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()


setup(
    name='whitespace',
    version=version,
    description='A Whitespace interpreter',
    long_description=readme,
    url='https://github.com/dwayne/whitespace-python',
    author='Dwayne Crooks',
    author_email='me@dwaynecrooks.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Interpreters'
    ],
    keywords='whitespace',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'whitespace=whitespace.cli:main'
        ]
    }
)
