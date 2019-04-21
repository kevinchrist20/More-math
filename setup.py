from setuptools import setup, find_packages

setup(name='Moremath',
      version='0.1',
      url='https://github.com/kevinchrist20/More-math.git',
      license='MIT',
      author='Kevin Christian',
      author_email='codemonk227@protonmail.com',
      description='Additional math library',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read())
