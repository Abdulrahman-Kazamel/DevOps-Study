

Need visibility for:
- CPU - memory - pod health - logs - metrics - alerts

---

# Metrics Server

Provides resource metrics.

Used by:

- HPA - kubectl top

---

# View Metrics

```
kubectl top pods
```

---

# Logging Architecture

```
Container Logs -> Node Logs -> Log Collector -> Central Platform
```

---

# Popular Monitoring Stack

|Tool|Purpose|
|---|---|
|Prometheus|metrics|
|Grafana|dashboards|
|Loki|logs|
|AlertManager|alerts|

---

# Prometheus

collects metrics from: ( - nodes - pods - services )

Works using pull model.

---

# Grafana

visual dashboards for: ( - CPU - memory - response time - node health )

---

# AlertManager

sends alerts using: (- email - Slack - Teams)

---

# Loki

log aggregation system.


---

# 18 - Observability Stack

# What is Observability?

Understanding system state using:

|Pillar|Purpose|
|---|---|
|Metrics|numbers|
|Logs|events|
|Traces|request flow|

```bash
# Metrics Example

CPU usage = 80%
memory = 70%


# Logs Example

user login failed
database timeout


# Tracing Example
#Tracks request between services.


frontend --> api -->  auth-service -->  database
```



# Popular Observability Stack

|Tool|Purpose|
|---|---|
|Prometheus|metrics|
|Grafana|dashboards|
|Loki|logs|
|Tempo|tracing|
|Jaeger|tracing|
|OpenTelemetry|telemetry standard|
