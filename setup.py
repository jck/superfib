from setuptools import setup

setup(
    name='superfib',
    author='Keerthan Jaic',
    author_email='jckeerthan@gmail.com',
    description='',
    # version=version,
    # url='http://github.com/jck/superfib',
    packages=['superfib'],
    install_requires=['click'],
    entry_points='''[console_scripts]
                    superfib=superfib.cli:main
                    ''',
    # classifiers=[
    #     'License :: OSI Approved :: BSD License',
    #     'Programming Language :: Python',
    #     'Programming Language :: Python :: 3',
    # ],
)
