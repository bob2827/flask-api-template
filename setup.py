from setuptools import setup, find_packages

#Reference on setuptools usage
#https://pythonhosted.org/an_example_pypi_project/setuptools.html

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
      install_requires=['flask', 'SQLAlchemy', 'redis', 'wtforms',
                        'flask-restful', 'mysql-python', 'requests'],
      zip_safe=False,
     )
