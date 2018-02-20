import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='behave-catalog',
    zip_safe=False,
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='Produce a searchable HTML page listing steps available '
                'to use within .feature files, along with corresponding '
                'function docstrings.',
    long_description=README,
    url='https://github.com/teapow/behave-catalog',
    author='Thomas Power',
    author_email='thomaspwr@gmail.com',
    classifiers=[],
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
