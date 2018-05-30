from setuptools import setup, find_packages

setup(
    name='carpe_diem',
    version='0.1.0',
    description='Carpe Diem plot generator',
    url='https://github.com/gaborvecsei',
    author='Gabor Vecsei',
    author_email='vecseigabor.x@gmail.com',
    license='MIT',
    install_requires=['matplotlib', "numpy"],
    packages=["carpe_diem"],
    entry_points={
        'console_scripts': [
            'carpe_diem = carpe_diem.plot_generator:create'
        ]
    }
)
