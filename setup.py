from setuptools import setup

import notifyme


setup(
    name='notifyme',
    version='0.1',
    description=notifyme.__doc__.strip(),
    url='https://github.com/djbelyak/NotifyMeBot',
    author='Ivan Belyavtsev',
    author_email='djbelyak@gmail.com',
    license='MIT',
    packages=['notifyme'],
    entry_points={
        'console_scripts': ['notifyme = notifyme.__main__:main']
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Topic :: Communications :: Chat',
        'Topic :: System :: Logging',
        'Topic :: System :: Monitoring',
        'Topic :: Software Development',
        'Topic :: System :: Networking',
        'Topic :: Terminals',
        'Topic :: Text Processing',
        'Topic :: Utilities'
    ]
)
