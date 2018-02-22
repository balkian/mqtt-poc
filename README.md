Testing three different MQTT brokers: mosquitto, hbmqtt (python) and volantmq (go).
The goal is to compare different brokers using the same client code.
In particular, I wanted to know if the main python and golang broker implementations support QOS level 2 subscriptions.
i.e. whether the broker will store undelivered messages while the subscriber is offline, and deliver them once it comes online.

The compose file sets up the three brokers, and two clients (a producer and a consumer).

## Setup

Before you launch the clients, launch the brokers you want to try with compose.
This will launch the three brokers:

```
docker-compose up mosquitto pybroker gobroker
```


## Clients

The clients can be configured to use different brokers with the `MQTT_HOST` environment variable (see below).
You can run as many clients as you wish.

### Mosquitto

```
docker-compose run -e MQTT_HOST=mosquitto consumer
```

```
docker-compose run -e MQTT_HOST=mosquitto producer
```

### HBMQTT (python)

This broker is using BoltDB (an embedded key-value store) for persistence.

```
docker-compose run -e MQTT_HOST=pybroker consumer
```

```
docker-compose run -e MQTT_HOST=pybroker producer
```

### VolantMQ (Go)

```
docker-compose run -e MQTT_HOST=gobroker consumer
```

```
docker-compose run -e MQTT_HOST=gobroker producer
```
