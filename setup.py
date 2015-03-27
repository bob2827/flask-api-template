from setuptools import setup, find_packages

#Reference on setuptools usage
#https://pythonhosted.org/an_example_pypi_project/setuptools.html

#Needed ubuntu packages:
#sudo apt-get install libmysqlclient-dev

setup(name='apitemplate',
      version='0.1',
      description='API Template',
      author='Bob Sherbert',
      author_email='bob@carbidelabs.com',
      packages=['apitemplate'],
      package_data={'apitemplate': ['templates/*ml', 'static/img/*',
                                'static/css/*', 'static/js/*'],
                   },
      scripts = [],
      dependency_links=['http://github.com/bob2827/pydis/tarball/master#egg=pydis'],
      install_requires=['Flask', 'SQLAlchemy', 'redis', 'wtforms',
                        'flask-restful', 'mysql-python', 'requests', 'pydis'],
      zip_safe=False,
     )
