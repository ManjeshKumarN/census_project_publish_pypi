from setuptools import setup, find_packages

setup(
     name="tfx-deep-learning-continous-training-pipeline",
    license="MIT",
    version="0.0.1",
    description="""
    This project is created to provide a simple way to
    ingest data from the Census API.
    https://files.consumerfinance.gov/ccdb/complaints.csv.zip

    Project provide prebuilt airflow DAG pipleine designed using TFX.
    
    how to use this library

    ```
    from census_consumer_complaint_orchestrator.airflow_orchestrator import get_airflow_dag_pipeline
    dag = get_airflow_dag_pipeline()
    ```


    """,
    author="Manjesh Kumar",
    packages=find_packages(),
    install_requires=['tfx==1.6.1', 'apache-beam[interactive]', 'apache-airflow']
)
