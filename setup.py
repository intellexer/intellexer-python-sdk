import setuptools


setuptools.setup(
	name='intellexer',
	version='1.0',
	description='Intellexer python SDK',
	license='MIT',
	author='Effective Soft',
	author_email='kai3341@mail.ru',
	url='https://github.com/kai3341/intellexer-python',
	download_url='https://github.com/kai3341/intellexer-python/archive/1.0.zip',
	keywords=('API', 'NLP', 'INTELLEXER'),
	packages=setuptools.find_packages(),
	install_requires=['urllib3'],
	classifiers=(
		# "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Build Tools',
		'License :: OSI Approved :: MIT License',

		#Specify which pyhton versions that you want to support
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
	),
)
