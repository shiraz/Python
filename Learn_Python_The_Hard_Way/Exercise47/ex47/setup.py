try:
	from setuptools import setup
except:
	from disutils.core import setup

config = {
'description': 'My Project',
'author': 'My Name',
'url': 'URL to get it at.',
'download_url': 'Where to download it.',
'author_email': 'My email.',
'version': '0.1',
'install_requires': ['nose'],
'packages': ['ex47'],
'scripts': [],
'name': 'projectname'
}

setup(**config)
