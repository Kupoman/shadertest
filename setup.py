from setuptools import setup

def readme():
    with open('README.md') as readme_file:
        return readme_file.read()

setup(
    name='shadertest',
    version='0.1.0',
    author='Daniel Stokes',
    author_email='stokes.daniel.j@gmail.com',
    url='https://github.com/Kupoman/shadertest',
    description='A pyhton library for unit testing GLSL functions',
    long_description=readme(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Testing',
    ],
    keywords='glsl unit test',
    packages=['shadertest'],
    install_requires=[
        'PyOpenGL',
        'PySDL2',
    ],
)
