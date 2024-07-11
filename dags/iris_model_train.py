
import textwrap
from datetime import datetime, timedelta

from iris_ml.operations import load_data  # , post_model, train_step

# The DAG object; we'll need this to instantiate a DAG
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator

with DAG(
    "iris_model_train",
    tags=["iris_ml"],
    schedule=None,
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        "retries": 0,
    },
    description="Train iris multiclass model",
    catchup=False,
) as dag:

    t1 = PythonOperator(
        task_id="load_data",
        python_callable=load_data.load_data
    )
    t1.doc_md = 'Load Iris data set'

    t1
    '''
    t2 = PythonOperator(
        task_id="train_step",
        python_callable=train_step
    )
    t2.doc_md = 'Train a model to classify syntethic data'

    t3 = PythonOperator(
        task_id="post_model",
        python_callable=post_model
    )
    t3.doc_md = 'Save model in models/'

    t1 >> t2 >> t3
'''
