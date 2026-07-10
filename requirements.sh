#!/bin/bash
set -e

echo "==== Actualizando sistema ===="
sudo apt update && sudo apt upgrade -y

echo "==== Instalando herramientas base ===="
sudo apt install -y python3-pip python3-venv git

echo "==== Creando entorno virtual .pacon ===="
if [ ! -d ".pacon" ]; then
    python3 -m venv .pacon
fi

echo "==== Activando entorno ===="
source .pacon/bin/activate

echo "==== Actualizando pip ===="
pip install --upgrade pip setuptools wheel

echo "==== Instalando librerías de Ciencia de Datos ===="
pip install \
numpy \
pandas \
scikit-learn \
matplotlib \
seaborn \
jupyterlab \
notebook \
ipywidgets \
joblib \
tqdm \
pillow

echo "==== Verificando instalaciones ===="
python3 -c "import numpy; print('NumPy OK')"
python3 -c "import pandas; print('Pandas OK')"
python3 -c "import matplotlib; print('Matplotlib OK')"
python3 -c "import sklearn; print('Scikit-learn OK')"
python3 -c "import seaborn; print('Seaborn OK')"
python3 -c "from PIL import Image; print('Pillow OK')"

echo "==== Setup completo listo ===="
echo "Activa el entorno con: source .pacon/bin/activate"
