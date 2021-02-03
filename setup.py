import setuptools

with open('README.md', 'r', encoding = 'utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'GuruStock',
    version = '1.0.0',
    author = 'Vitor Leonardo Pauloski',
    author_email = 'vitorleonardo.pauloski@gmail.com',
    description = "GuruStock is a Python package for extracting market data from Guru app.",
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/vitorpauloski/GuruStock',
    packages = ['guru'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Topic :: Office/Business :: Financial :: Investment'
    ],
    python_requires = '>=3.8',
    install_requires = ['requests>=2.25.1'],
)
