from distutils.core import setup

setup(
  name = 'DeepSentiment',
  packages = ['DeepSentiment'],
  version = '0.1.0',
  description = 'Python wrapper for Sentiment Analysis leveraging Stanford CoreNLP',
  author = 'Abhinav Bhatnagar',
  author_email = 'abhatnagar.1610@gmail.com',
  url = 'https://github.com/AbhinavBhatnagar/DeepSentiment',
  download_url = 'https://github.com/AbhinavBhatnagar/DeepSentiment/tarball/',
  keywords = ['nlp'],
  classifiers = [],
  install_requires = ['requests','json']
)