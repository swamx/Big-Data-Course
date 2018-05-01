#!/bin/bash
gnome-terminal -e "bash /home/fartingfox/kafka/bin/kafka-server-stop.sh"
gnome-terminal -e "bash /home/fartingfox/kafka/bin/zookeeper-server-stop.sh"
gnome-terminal -e "bash /home/fartingfox/hadoop/sbin/stop-dfs.sh"
