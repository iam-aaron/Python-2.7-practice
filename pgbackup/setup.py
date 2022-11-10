from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='pgbackup',
    version='1.0',
    description='Database backup for S3 or local.',
    long_description=readme,
    author='Aaron Medina',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[]
)
