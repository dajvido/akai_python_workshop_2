from setuptools import setup

setup(
    name='calc_chriss',
    version='1.0.2',
    description='AKAI calculatorA',
    author='<yournick>',
    packages=['calc', ],
    install_requires=[], #list of dependencies
    entry_points = {
        "console_scripts" : ["my_calc = calc:main",]
    },
)
