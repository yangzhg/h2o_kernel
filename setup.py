from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name='h2o_kernel',
    version='1.0.1',
    packages=['h2o_kernel'],
    description='H2o kernel for Jupyter',
    long_description=readme,
    author='Yang Zhengguo',
    author_email='yangzhengguo01@baidu.com',
    url='https://github.com/yangzhg/h2o_kernel',
    install_requires=[
        'h2o', 'IPython', 'ipykernel'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
    ],
)
