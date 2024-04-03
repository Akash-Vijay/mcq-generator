from setuptools import setup, find_packages

setup(
  name="mcq-gen",
  version="0.1",
  packages=find_packages(),
  install_requires=["langchain", "langchain-google-genai", "streamlit", "python-dotenv", "pyPDF2"],
  author="Akash Vijay",
  author_email="akashvijay789@gmail.com"
)