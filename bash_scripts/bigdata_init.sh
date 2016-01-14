#!/bin/bash

#*/2 * * * * /home/bigdata/prototype_init.sh  #every two minutes to run besure to stop it after the job is running
#or
#sudo /etc/init.d/crond stop   #then sudo crontab -e

#start hadoop
start-all.sh
#zookeeper
/usr/local/zookeeper/zookeeper-3.4.6/bin/zkServer.sh
gnome-terminal --working-directory=/usr/local/kafka/kafka_2.10-0.8.2.1 -e "./bin/kafka-server-start.sh config/server.properties" && echo "broker 1 has started"

#start a terminal of kafka broker server 1
gnome-terminal --working-directory=/usr/local/kafka/kafka_2.10-0.8.2.1 -e "./bin/kafka-server-start.sh config/server-1.properties" && echo "broker 2 has started"
#gnome-terminal -e  ./bin/kafka-server-start.sh config/server.properties &&

#start a terminal of kafka broker server 2
gnome-terminal --working-directory=/usr/local/kafka/kafka_2.10-0.8.2.1 -e "./bin/kafka-server-start.sh config/server-2.properties" && echo "broker 3 has started"


#hbase
#get hbase running
/usr/local/hbase/hbase-1.1.2/bin/start-hbase.sh && echo "hbase daemon has started"

#get the thrift server running
gnome-terminal --working-directory=/usr/local/hbase/hbase-1.1.2/bin -e "hbase thrift start" && echo "thrift is running"




#kafka


#start a producer this producer will make an infinite loop of message stamping into spark steaming
gnome-terminal -e "python /home/bigdata/simpleproducer.py"

#start a consumer
gnome-terminal -e "python /home/bigdata/simpleconsumer.py"

#spark streaming


#run spark streaming
bin/spark-submit --jars   /home/bigdata/spark_kafka/spark-streaming-kafka-assembly_2.10-1.5.1.jar   /home/bigdata/spark_kafka/kafka_wordcount.py   localhost:2182 test1



#Go to /usr/local/kafka/kafka..
#In order to have kafka running,
#zookeeper must be running

#bin/zookeeper-server-start.sh config/zookeeper.properties
#broker must be running
#    bin/kafka-server-start.sh config/server.properties
#bin/kafka-server-start.sh config/server-1.properties
#define a topic/ create one
#    bin//kafka-topic.sh --create --zookeeper localhost:2181 --replication-factor 2 --partitions 3 --topic test1
#a producer must present
#    bin/kafka -console-producer.sh --broker-list localhost:9092 --topic test1
#a consumer must present
#bin/kafka-console-consumer.sh --zookeeper localhost:2181 --topic test1 --from-begining
