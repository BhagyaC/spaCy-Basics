# spaCy-Basics
Basic implementation with spacy

spaCy is a free, open-source library for advanced Natural Language Processing (NLP) in Python.

spaCy is designed specifically for production use and helps you build applications that process and “understand” large volumes of text. It can be used to build information extraction or natural language understanding systems, or to pre-process text for deep learning.

Installation

install spaCy in a virtual environment

pip install virtualenv or pip install --user virtualenv

sudo pip3 install virtualenv virtualenvwrapper
sudo rm -rf ~/get-pip.py ~/.cache/pip

echo -e "\n# virtualenv and virtualenvwrapper" >> ~/.bash_profile
echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bash_profile
echo "export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3" >> ~/.bash_profile
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bash_profile

workon cv Hence the virtual environment well setted

python -m spacy download en    //install spaCy and its English-language model before proceeding further
