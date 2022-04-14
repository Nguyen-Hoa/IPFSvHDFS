docker service create \
	--replicas 1 \
	--name proxy_docker \
	--network hdfs-net \
	-p 7001:7001 \
	newnius/docker-proxy
