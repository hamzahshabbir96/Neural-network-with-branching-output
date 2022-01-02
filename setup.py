import setuptools

setuptools.setup(
  include_package_data=False,
  name='MyDeepNet',
  version='0.0.1',
  url='https://github.com/hamzahshabbir96/Neural-network-with-branching-output',
  description='Neural network module with branching output'
  author='Hamzah Shabbir',
  author_email='hamzahshabbir7@gmail.com',
  packages=setuptools.find_packages(),
  install_requires=['numpy','math'],
  long_description='A neural network modeule which allows to branch out multiple output at different layers for classification with customizable layers and options of choosing hyperparameters ',
  long_description_context_type='text/markdown',
  keywords=['Neural Network','Classification','Python','Neurons','layers'],
   classifiers=[
          'Development Status :: Planning',
          'Environment :: Win32 (MS Windows)',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development',
          'Topic :: Deep Neural network',
      ]
  


)
