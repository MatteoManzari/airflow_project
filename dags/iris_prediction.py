
import textwrap
from datetime import datetime, timedelta

from iris_ml.operations import load_data

# The DAG object; we'll need this to instantiate a DAG
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator

# from iris_ml.operations import load_data, post_results, predict_class

with DAG(
    "iris_prediction",
    tags=["iris_ml"],
    schedule=None,  # "@daily",
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        "retries": 0,
    },
    description="Predict flower spiecies for new data",
    catchup=False,
) as dag:

    t1 = PythonOperator(
        task_id="load_data",
        python_callable=load_data.load_data)
    t1.doc_md = 'Load Iris data and create new Synthetic data'

    '''    
    t2 = PythonOperator(
        task_id="predict_class",
        python_callable=predict_class
    )
    t2.doc_md = 'Use a pretrained model to classify syntethic data'

    t3 = PythonOperator(
        task_id="post_results",
        python_callable=post_results
    )
    t3.doc_md = 'Save results in a csv file'

    t1 >> t2 >> t3
'''
