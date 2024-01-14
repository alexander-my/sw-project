ToDo:
1. Dockerfile
2. Dockerfile for creation database
3. Ansble for autocreation containers
4. Ci/Cd pipeline
----------------------------------------
4. Helm-chart for project
5. Refactor IaC and ci/cd
----------------------------------------
6. Monitoring
7. Logs collecting
8. Trivi
9. Sonarqube 


docker run -d --name ch-server --ulimit nofile=262144:262144 -p 8123:8123 -p 9000:9000 -p 9009:9009 yandex/clickhouse-server