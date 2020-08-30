# pip install -r './resources/requirements.txt'
# export PYTHONPATH=/opt/anaconda3/lib/python3.7/site-packages
# rm -rf venv


sudo killall -9 Python
python3 -m venv venv
source "./venv/bin/activate"
pip install --upgrade pip
pip install flask
pip install pandas
pip install bs4
pip install splinter
pip install nltk
pip install sklearn
pip install gensim
pip install matplotlib
pip install sqlalchemy
pip install python-dotenv
# pip install jsonify
python3 app.py
