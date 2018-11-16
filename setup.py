from distutils.core import setup
 
setup(
    name='check_influx',
    version="1.1.1",
    packages=['src'],
    install_requires=['influxdb', 'NagAconda'],
    license='MIT',
    url="https://github.com/dolbyjoab/check_influx.git",
    description='Nagios plugin for querying stats from InfluxDB',
    author='Etienne Delsy',
    author_email='dolbyjoab at gmail com',
    scripts=['src/check_influx']
)
