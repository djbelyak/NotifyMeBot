from setuptools import setup


setup(
    name='notifymebot',
    version='0.1',
    description='Command launcher with status notifications via Telegram',
    url='https://github.com/djbelyak/NotifyMeBot',
    author='Ivan Belyavtsev',
    author_email='djbelyak@gmail.com',
    license='MIT',
    packages=['notifyme'],
    entry_pints={
        'notifyme': ['notifyme:main']
    },
    zip_safe=True
)
