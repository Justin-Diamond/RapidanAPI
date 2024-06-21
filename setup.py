from setuptools import setup, find_packages

setup(
    name='RapidanAPI',
    version='1.0.43',
    packages=find_packages(),
    description='RapidanAPI allows Rapidan Energy Group\'s clients to conveniently pull energy data.',
    long_description=open('README_PYPI.md').read(),
    install_requires=[
        'requests',
        'pandas',
    ],
    url='https://github.com/Justin-Diamond/RapidanAPI',
    author='Justin Diamond',
    author_email='justin.diamond@rapidanenergy.com'
)
