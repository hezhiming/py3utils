from setuptools import setup

setup(name='py3utils',
      description='Useful Python 3.5 utils',
      version='0.1',
      url='https://github.com/hezhiming/py3utils',
      author='hezhiming',
      author_email='he.zhiming@foxmail.com',
      license='MIT',
      classifiers=[
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: Implementation :: CPython',
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
