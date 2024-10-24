## ML Flow basic Operation 

## For Dagshub 

import dagshub

dagshub.init(repo_owner='maushamkumar', repo_name='Chest-Cancer-Project', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)


```bash
export MLFLOW_TRACKING_URI = https://dagshub.com/maushamkumar/Chest-Cancer-Project.mlflow

export MLFLOW_TRACKING_USERNAME = Mausham-Kumar

export MLFLOW_TRACKING_PASSWORD = 


```