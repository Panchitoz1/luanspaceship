import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
        name='luanspaceship',
        version='0.0.0',
        author='Francisco Carrasco Varela',
        author_email='ffcarrasco@uc.cl',
        description='Prints an ASCII spaceship given an integer via flag \'-length\'',
        long_description=long_description,
        long_description_content_type='text/markdown',
        packages=setuptools.find_packages(),
        install_requires=[
            'absl-py',
            'pyperclip'
            ],
        classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
        entry_points='''
        [console_scripts]
        luanspaceship=LuanSpaceship.command_line:run_cli
        '''
        )
