#!/bin/bash
gnome-terminal -e "bash /home/fartingfox/kafka/bin/zookeeper-server-start.sh /home/fartingfox/kafka/config/zookeeper.properties"
gnome-terminal -e "bash /home/fartingfox/kafka/bin/kafka-server-start.sh /home/fartingfox/kafka/config/server.properties"
gnome-terminal -e "bash /home/fartingfox/hadoop/sbin/start-dfs.sh"
gnome-terminal -e "mongod --dbpath /home/fartingfox/data/mongo/data --logpath /home/fartingfox/data/mongo/log --port 27017 --logappend"
