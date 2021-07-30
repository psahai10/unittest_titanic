from setuptools import setup, find_packages

setup(name="titanic_linear_regression",
      version="0.1.0",
      description="Univariate linear regression of titanic survival",
      author="Pankaj Sahai",
      packages=find_packages("src"),
      package_dir={"": "src"},
      author_email="psahai10@gmail.com",
      install_requires=["jupyter==1.0.0",
                        "matplotlib==3.1.1",
                        "numpy==1.17.3",
                        "pytest==5.2.2",
                        "pytest-mpl==0.10",
                        "pytest-mock==1.11.2",
                        "scipy==1.3.1",
                        ],
      )