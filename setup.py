import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='behave-catalog',
    zip_safe=False,
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='Generate a searchable HTML page listing steps available '
                'to use within .feature files, along with corresponding '
                'function docstrings.',
    long_description=README,
    url='https://github.com/teapow/behave-catalog',
    author='Thomas Power',
    author_email='thomaspwr@gmail.com',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.3',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Documentation',
    ],
    install_requires=[
        'behave',
        'jinja2',
    ],
    entry_points={
        'console_scripts': [
            'behave-catalog = behave_catalog.__main__:main',
        ],
    }

)
