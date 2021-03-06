from setuptools import setup, find_packages

setup(name="titanic_linear_regression",
      version="0.1.0",
      description="Univariate linear regression of titanic survival",
      author="Pankaj Sahai",
      packages=find_packages("src"),
      package_dir={"": "src"},
      author_email="psahai10@gmail.com",
      install_requires=['attrs==21.2.0',
                        'iniconfig==1.1.1',
                        'numpy==1.21.1',
                        'packaging==21.0',
                        'pandas==1.3.1',
                        'pandas-summary==0.0.7',
                        'pluggy==0.13.1',
                        'py==1.10.0',
                        'pyparsing==2.4.7',
                        'pytest==6.2.4',
                        'python-dateutil==2.8.2',
                        'pytz==2021.1',
                        'six==1.16.0',
                        'toml==0.10.2'
                        ],
      )