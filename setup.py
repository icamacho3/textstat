from setuptools import setup
from io import open

setup(
    name='textstat',
    packages=['textstat'],
    version='0.5.6',
    description='Calculate statistical features from text',
    author='Shivam Bansal, Chaitanya Aggarwal',
    author_email='shivam5992@gmail.com',
    url='https://github.com/shivam5992/textstat',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    package_data={'': ['easy_word_list']},
    include_package_data=True,
    install_requires=['pyphen', 'repoze.lru'],
    license='MIT',
    classifiers=(
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        ),
)
