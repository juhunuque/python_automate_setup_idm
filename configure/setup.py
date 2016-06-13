from setuptools import setup, find_packages

setup(
    name='Automate Script',
    version='1.0.1',

    install_requires=[
        'PyJWT',
        'cryptography',
        'requests',
        'PyYaml',
        'cherrypy',
        'beaker',
        'funcsigs',
        'six'
    ],



    author='Julio Nunez',
    license='MIT',
)
