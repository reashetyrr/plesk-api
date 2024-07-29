from setuptools import setup

setup(
    name='plesk-api',
    version='0.0.1',
    packages=['plesk', 'plesk.definitions', 'plesk.classes'],
    license='MIT',
    description='A simple API wrapper for Plesk',
    url='https://www.github.com/reashetyrr/plesk-api',
    author='Reashetyrr',
    author_email="webmaster@reashetyr.software",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'requests',
    ],
    scripts=[],
    keywords=['plesk'],
)
