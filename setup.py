from setuptools import setup

setup(
        install_requires=[],#'sys' 
        entry_points={
            "console_scripts":[
                "myapp = test:ggg"
            ]
        }
)