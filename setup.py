from setuptools import setup

setup(name='osrm_plus',
      version='0.1',
      description='Allow to retrieve both distance and duration matrix for an input list of OSRM coordinates.',
      url='https://github.com/cglacet/osrm_plus',
      author='Christian Glacet',
      author_email='christian.glacet@gmail.com',
      license='MIT',
      packages=['osrm_plus'],
      zip_safe=False,
      install_requires=[
        "requests >= 2.0.0",
        "numpy >= 1.0.0",
        "clique_tour >= 0.21.0"
    ])
