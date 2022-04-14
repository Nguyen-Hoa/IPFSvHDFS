docker service create \
	--name hadoop-master \
	--network hdfs-net \
	--hostname hadoop-master \
	--constraint node.role==manager \
	--replicas 1 \
	--endpoint-mode dnsrr \
	newnius/hadoop:2.7.4