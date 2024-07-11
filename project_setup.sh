mkdir airflow

pip3 install virtualenv -v
python3 -m virtualenv project_env
source ./project_env/bin/activate           

pip install -r requirements.txt


PROJECT_DIR="$(pwd)/airflow"
export AIRFLOW_HOME=$PROJECT_DIR

airflow standalone