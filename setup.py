from setuptools import setup, find_packages
import sys, os

version = '0.3'

f = open('doc/README.txt')
readme = f.read()
f.close()

f = open('doc/CHANGES.txt')
changes = f.read()
f.close()

setup(name='dateable.kalends',
      version=version,
      description="Dateable calendaring API",
      long_description=readme + '\n\n' + changes,
      classifiers=[
          'Framework :: Zope3',
          'Framework :: Plone',
          'Programming Language :: Python',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Topic :: Software Development :: Libraries :: Python Modules',
          ],
      keywords='Dateable Calendaring',
      author='Lennart Regebro',
      author_email='regebro@gmail.com',
      url='http://plone.org/products/dateable',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['dateable'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
