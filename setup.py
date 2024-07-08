from setuptools import setup, find_packages

setup(
    name='RapidanAPI',
    version='1.0.53',
    packages=find_packages(),
    description='RapidanAPI allows Rapidan Energy Group\'s clients to conveniently pull energy data.',
    long_description=open('README_PYPI.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'requests',
        'pandas',
    ],
    extras_require={
        'dev': [
            'flake8',
            'twine',
            'wheel'
        ],
    },
    url='https://github.com/Justin-Diamond/RapidanAPI',
    author='Justin Diamond',
    author_email='justin.diamond@rapidanenergy.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
