# IoT-Data-Monitoring-Visualization-System

### Run docker
    - Terminal 1: docker-compose up -d
    - Terminal 2: cd/simulator
                  python publisher.py
    - docker ps  (check running)


### Verify in InfluxDB UI
Go to -> http://localhost:8086 → Data Explorer
- Login with
    Username: admin
    Password: admin123
- Then select:
    Bucket → my-bucket
    Measurement → it will appear automatically if Telegraf wrote something (e.g. mqtt_consumer)

### Connect Grafana
In Grafana: http://localhost:3000/
- Go to Data Sources → InfluxDB
    URL: http://influxdb:8086
    Organization: my-org
    Token: my-super-token
    Default Bucket: my-bucket
    Click Save & Test
- Then create a new dashboard:
    Query example (Flux):
    from(bucket: "my-bucket")
      |> range(start: -10m)
      |> filter(fn: (r) => r._measurement == "mqtt_consumer")

### Stop containers
    - docker-compose down
    - docker-compose down -v
    - docker-compose up -d  (start again)
