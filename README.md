# covid_mlops

mlflow commands: 
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts --host 0.0.0.0 -p 1234

create local remote storage:
mkdir -p /tmp/dvc
dvc remote add -d myremote /tmp/dvc