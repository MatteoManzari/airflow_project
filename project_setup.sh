chmod +x your_script.sh
pip3 install virtualenv -v
python3 -m virtualenv project_env
chmod +x project_env/bin/activate
source ./project_env/bin/activate           
pip install -r requirements.txt

PROJECT_DIR="$(pwd)"
export AIRFLOW_HOME=$PROJECT_DIR

airflow standalone