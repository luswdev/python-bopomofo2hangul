import os
import re
from setuptools import find_packages, setup
setuptools_kwargs = {
    'install_requires': [
    "requirements.txt"
    ],
    'zip_safe': False,
}

current_dir = os.path.dirname(os.path.realpath(__file__))

def get_meta():
    meta_re = re.compile(r"(?P<name>__\w+__) = '(?P<value>[^']+)'")
    meta_d = {}
    with open(os.path.join(current_dir, 'pybopomofo2hangul/__init__.py'),
              encoding='utf8') as fp:
        for match in meta_re.finditer(fp.read()):
            meta_d[match.group('name')] = match.group('value')
    return meta_d

meta_d = get_meta()
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name='pybopomofo2hangul',
    version=meta_d['__version__'],
    packages=find_packages(),
    long_description_content_type="text/markdown",
    long_description=long_description,
    author=meta_d['__author__'],
    author_email='callumlu@gmail.com',
    license=meta_d['__license__'],
    url='https://github.com/luswdev/python-bopomofo2hangul',
    keywords=['bopomofo', 'hangul'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities',
        'Topic :: Text Processing',
    ],
    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, <4',
    **setuptools_kwargs
)