1) Поднять сборку airflow (sudo docker compose up  airflow-init, sudo docker compose up)
2) Поднять сборку spark (просто sudo docker compose up в папке спарка)
3) В контейнерах airflow через пользователя root (sudo docker exec -u root -it {container_name} /bin/bash) >> sudo pip install apache-airflow-providers-apache-spark
4) Подключить контейнеры спарка к сети аирфлоу (docker inspect {airflow_spark_default} затем docker network {airflow_spark_default} spark-master/spark-worker)
5) Добавить конекшн на спарк в аирфлоу (опционально) (у меня нет Spark connection в аирфлоу)
6) поставить jdk на worker airflow (sudo apt-get install -y openjdk-17-jdk). Если не получается с первого раза сделать apt-get update
