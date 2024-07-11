mkdir airflow

pip3 install virtualenv -v
python3 -m virtualenv project_env
source ./project_env/bin/activate           

pip install -r requirements.txt

#remove examples dags
rm project_env/lib/python3.9/site-packages/airflow/example_dags/*.py

#setting up environment variables
DAGS_DIR="$(pwd)/dags"
AIRFLOW_DIR="$(pwd)/airflow"
export AIRFLOW_HOME=$AIRFLOW_DIR
export AIRFLOW__CORE__DAGS_FOLDER=$DAGS_DIR

#run airflow in dev mode
airflow standalone