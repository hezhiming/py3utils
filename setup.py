from setuptools import setup

setup(name='py3utils',
      description='Useful Python 3.5 utils',
      version='0.1',
      url='https://github.com/hezhiming/py3utils',
      author='hezhiming',
      license='MIT',
      classifiers=[
          'Intended Audience :: Develpers',
          'License :: OSI Approved :: MIT',
          'Programming Language :: Python :: 3'
      ],
      packages=['py3utils'],
      install_requires=[
          'python-dateutil>=2.5.0'
      ],
      # entry_points={
      #     'console_scripts': [
      #         'encrypt=crytto.main:run'
      #     ]
      # }

      )
