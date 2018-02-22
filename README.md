Testing three different MQTT brokers: mosquitto, hbmqtt (python) and volantmq (go).

The compose file sets up the three brokers, and two clients (a producer and a consumer).

## Setup

To launch the three brokers, run:

```
docker-compose up mosquitto pybroker gobroker
```

The brokers can be configured to use different brokers with the `MQTT_HOST` environment variable (see below).

## Mosquitto

```
docker-compose run -e MQTT_HOST=mosquitto consumer
```

```
docker-compose run -e MQTT_HOST=mosquitto producer
```

## HBMQTT (python)

This broker is using BoltDB (an embedded key-value store) for persistence.

```
docker-compose run -e MQTT_HOST=pybroker consumer
```

```
docker-compose run -e MQTT_HOST=pybroker producer
```

## VolantMQ (Go)

```
docker-compose run -e MQTT_HOST=gobroker consumer
```

```
docker-compose run -e MQTT_HOST=gobroker producer
```
