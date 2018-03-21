from setuptools import setup

setup(
    name='snapshotanalyser-30000',
    version='0.1',
    author='Nigel Scragg',
    author_email='nscraggitpro@googlemail.com',
    description="SanpshotAnalyser 30000 is a tool to manage AWS EC2 snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/devops4startups/snapshotanalyser-30000",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',

)
