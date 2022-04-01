import setuptools

setuptools.setup(
        name='test',
        version='0.0.0',
        packages=setuptools.find_packages(),
        install_requires=[
            'absl-py',
            'pyperclip'
            ],
        entry_points='''
        [console_scripts]
        luanspaceship=LuanSpaceship.command_line:start
        '''
        )
