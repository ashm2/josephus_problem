from setuptools import setup
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='josephus_problem',
      version='0.1',
      description='Finds location of survivor in josephus problem',
      license='MIT',
      entry_points={
          'console_scripts': [
              'run = josephus:main'
          ]
      },
      install_requires=required,
      zip_safe=False)
