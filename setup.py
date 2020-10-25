import setuptools

with open("README.rst", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='Flask-MDE',
    version='1.2.1',
    url='https://github.com/bittobennichan/Flask-MDE',
    license='MIT',
    author='Bitto Bennichan',
    author_email='bittobennichan@protonmail.com',
    description='Pagedown for Flask',
    long_description=long_description,
    packages=['flask_mde'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'WTForms'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    python_requires='>=3.6',
    project_urls={
        'Documentation': 'https://flask-mde.readthedocs.io',
        'Source': 'https://github.com/bittobennichan/Flask-MDE',
    }
)
