from setuptools import setup

setup(
    name='datatool',
    version='0.1',
    description='Access and download remote datasets',
    url='https://github.com/matthew-brett/datatool',
    license='Modified BSD',
    packages=['datatool'],
    package_data={'datatool': ['tests/*.py',
                               'tests/data/*']},
    install_requires=['jsonpath-rw'],
    entry_points = {
        'console_scripts': ['datatool = datatool.command_line:main']
    }
)
