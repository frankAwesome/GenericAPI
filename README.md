# GenericAPI

### BUILD CMAKE ###
mkdir build && cd build && cmake .. && cmake --build . --target generate_models

docker compose
docker jenkins
docker service
docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=YourPasswordHere" -p 1433:1433 --name sqlserver-container -d mcr.microsoft.com/mssql/server:2019-latest
sudo docker run --cap-add SYS_PTRACE -e 'ACCEPT_EULA=1' -e 'MSSQL_SA_PASSWORD=password' -p 1433:1433 --name test -d mcr.microsoft.com/azure-sql-edge


docker run --platform=linux/arm/v7 --rm -it -p 15672:15672 -p 5672:5672 rabbitmq:3-management