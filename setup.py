import os
from distutils.core import setup

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name="jornada",
    version="0.1",
    author="",
    author_email="",
    description="jornada, based on GeoNode",
    long_description=(read('README.rst')),
    # Full list of classifiers can be found at:
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
    license="BSD",
    keywords="jornada geonode django",
    url='https://github.com/jornada/jornada',
    packages=['jornada',],
    install_requires=["geonode==2.0b12"],
    include_package_data=True,
    zip_safe=False,
)
