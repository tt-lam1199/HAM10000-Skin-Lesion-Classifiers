# CS171-ImageClassifier
# New Environment
conda create --name HAM10000-classifier python=3.11 -y
conda activate HAM10000-classifier
# Upgrade package installation tools
python -m pip install --upgrade pip setuptools wheel
# Install required packages
python -m pip install -r requirements_fixed.txt
# Register the envinronment
python -m ipykernel install --user --name HAM10000-classifier --display-name "Python 3.11 (HAM10000-classifier)"