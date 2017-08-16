from setuptools import setup

requirements = [
    'requests',
    'oauthlib',
    'requests_oauthlib',
    'click',
    'PyYAML',
    'pprint',
    'tabulate'
]
test_requirements = [ ]
setup(name='py3bitbucket',
      version='0.0.3',
      description='bitbucket client',
      author='Yo-An lin',
      author_email='yoanlin93@gmail.com',
      packages=['bitbucket'],
      license='MIT',
      scripts=['bin/bitbucket'],
      url='https://github.com/c9s/py-bitbucket',
      install_requires=requirements,
      tests_require=test_requirements
      )
