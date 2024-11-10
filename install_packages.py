import subprocess
import sys

# Lista das bibliotecas que precisam ser instaladas (excluídas as conhecidamente incompatíveis com Python 3.12.5)
required_packages = [
    "beautifulsoup4",   # BeautifulSoup
    "scrapy",           # Scrapy
    "selenium",         # Selenium
    "pandas",           # pandas
    "numpy",            # NumPy
    "scikit-learn",     # Scikit-Learn
    "spacy",            # SpaCy
    "matplotlib",       # matplotlib
    "seaborn",          # seaborn
    "plotly",           # plotly
    "scipy",            # SciPy
    "webdriver-manager",# webdriver-manager 
    "statsmodels",      # statsmodels
    "jupyter",          # jupyter
    "dash",             # Dash
    "openpyxl",         # openpyxl
    "xlsxwriter",       # xlsxwriter
    "pyspark",          # PySpark
    "pyarrow",          # PyArrow
    "pillow",           # Pillow (manipulação de imagens)
    "scikit-image",     # scikit-image (processamento de imagens)
    "python-docx",      # python-docx
    "nltk",             # NLTK
    "textblob",         # Textblob
    "gensim",           # Gensim
    "transformers",     # Transformers
    "altair",           # Altair
    "folium",           # Folium
    "pygal",            # Pygal
    "bokeh",            # Bokeh
    "xgboost",          # XGBoost
    "keras",            # Keras
]

# Função para instalar pacotes usando pip
def install_package(package):
    """Instala um pacote usando pip"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"{package} instalado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao instalar {package}: {e}")

# Função para exibir aviso sobre pacotes que exigem dependências de sistema
def system_dependency_warning(package, dependencies):
    print(f"AVISO: O pacote '{package}' requer as seguintes dependências do sistema: {', '.join(dependencies)}")
    print(f"Por favor, instale-as manualmente antes de tentar instalar '{package}'.")

# Verificar e instalar pacotes
def check_and_install_packages(packages):
    """Verifica se as bibliotecas estão instaladas e, se não estiverem, instala as ausentes"""
    for package in packages:
        package_name = package_map.get(package, package)  # Usa o nome correto para o import
        try:
            __import__(package_name)
            print(f"{package} já está instalado.")
        except ImportError:
            print(f"{package} não está instalado. Instalando agora...")
            install_package(package)

# Mapeamento dos nomes dos pacotes PyPI com os nomes usados no import
package_map = {
    "beautifulsoup4": "bs4",
    "webdriver-manager": "webdriver_manager",
    "pillow": "PIL",  # Pillow é importado como "PIL"
    "opencv-python": "cv2",  # OpenCV é importado como "cv2"
}

# Dependências de sistema para pacotes específicos
system_dependencies = {
    "pyaudio": ["libasound2-dev", "portaudio19-dev", "libportaudio2", "libportaudiocpp0"],
    "opencv-python": ["libopencv-dev", "python3-opencv"],
    "ffmpeg-python": ["ffmpeg"],
    "librosa": ["libsndfile1"],
    "pydub": ["ffmpeg"],
    "polyglot": ["libicu-dev", "pkg-config"],  # polyglot precisa dessas dependências para NER, etc.
}

# Verificação das dependências de sistema
def check_system_dependencies():
    for package, dependencies in system_dependencies.items():
        print(f"Verificando dependências do sistema para {package}...")
        system_dependency_warning(package, dependencies)

# Substituir pacotes pelo nome de import correto
def install_packages_for_python_version(packages):
    """Verifica a versão do Python e instala apenas pacotes compatíveis"""
    python_version = sys.version_info
    print(f"Versão do Python detectada: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    # Filtrar pacotes compatíveis apenas com Python >= 3.12
    if python_version.major == 3 and python_version.minor >= 12:
        compatible_packages = [pkg for pkg in packages if pkg not in ["tensorflow", "torch", "kivy", "kivymd"]]
        check_and_install_packages(compatible_packages)
    else:
        check_and_install_packages(packages)

# Instalar pacotes compatíveis com Python 3.12.5'
install_packages_for_python_version([package_map.get(pkg, pkg) for pkg in required_packages])

# Aviso sobre as dependências de sistema
check_system_dependencies()

print("Verificação e instalação de pacotes concluída.")
