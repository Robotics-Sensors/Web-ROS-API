from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    scripts=['src/bellande_3d_computer_vision_prediction.py'],
    packages=['ros_web_api_bellande_3d_computer_vision'],
    package_dir={'': 'src'},
)

setup(**setup_args)
