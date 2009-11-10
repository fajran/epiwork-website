from setuptools import setup, find_packages

setup(
    name = "epidb-website",
    version = "1.0",
    url = 'http://www.epiwork.eu/',
    license = 'BSD',
    description = 'EPIWork Database - Survey Website',
    author = 'Fajran Iman Rusadi',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
)
