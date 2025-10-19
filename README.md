1) Поднимаете сборку airflow (sudo docker compose up  airflow-init, sudo docker compose up)
2) Поднимаете сборку spark (просто sudo docker compose up в папке спарка)
3) заходите в контейнеры airflow через пользователя root (sudo docker exec -u root -it {container_name} /bin/bash) >> sudo pip install apache-airflow-providers-apache-spark
4) подключаете контейнеры спарка к сети аирфлоу (docker inspect {airflow_spark_s3_default} затем docker network {airflow_spark_s3_default} spark-master/spark-worker)
5) добавить конекшн на спарк в аирфлоу(опционально)
6) поставить jdk на worker airflow (sudo apt-get install -y openjdk-17-jdk). Если не получается с первого раза сделать apt-get update
