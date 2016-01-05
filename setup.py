from setuptools import setup, find_packages

setup(
    name='tep',
    packages=find_packages(),
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'tep = tep.__main__:main'
        ]
    },
)
