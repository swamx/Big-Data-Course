#!/bin/bash
gnome-terminal -e "bash /home/fartingfox/kafka/bin/zookeeper-server-start.sh /home/fartingfox/kafka/config/zookeeper.properties"
gnome-terminal -e "bash /home/fartingfox/kafka/bin/kafka-server-start.sh /home/fartingfox/kafka/config/server.properties"
