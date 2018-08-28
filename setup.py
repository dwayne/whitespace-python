from setuptools import setup


setup(
    entry_points={
        'console_scripts': [
            'whitespace=whitespace.cli:main'
        ]
    }
)
