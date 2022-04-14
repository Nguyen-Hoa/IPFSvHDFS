docker service create \
	--name hadoop-slave1 \
	--network hdfs-net \
	--hostname hadoop-slave1 \
	--replicas 1 \
	--endpoint-mode dnsrr \
    --detach=true \
	newnius/hadoop:2.7.4

docker service create \
	--name hadoop-slave2 \
	--network hdfs-net \
	--hostname hadoop-slave2 \
	--replicas 1 \
	--endpoint-mode dnsrr \
    --detach=true \
	newnius/hadoop:2.7.4

docker service create \
	--name hadoop-slave3 \
	--network hdfs-net \
	--hostname hadoop-slave3 \
	--replicas 1 \
	--endpoint-mode dnsrr \
    --detach=true \
	newnius/hadoop:2.7.4

docker service create \
	--name hadoop-slave4 \
	--network hdfs-net \
	--hostname hadoop-slave4 \
	--replicas 1 \
	--endpoint-mode dnsrr \
    --detach=true \
	newnius/hadoop:2.7.4