# Task for Cloud Platform Team at Sofia Tech Hub

## Objective

Create a simple Python service that checks the availability and response time of two external URLs, and exposes metrics in a Prometheus-compatible format.

## Requirements

- Create a Git repository (on GitHub or GitLab).
- Create a simple Python project that:
  - Queries two URLs:
    - `https://httpstat.us/503`
    - `https://httpstat.us/200`
  - Checks if the external URLs are up (HTTP status code `200`).
  - Measures and records the response time in milliseconds.
- The service should:
  - Run a simple HTTP server.
  - Produce Prometheus-formatted metrics at a service URL endpoint.

### Expected Prometheus Metrics Output Example:

```text
sample_external_url_up{url="https://httpstat.us/503"} = 0
sample_external_url_response_ms{url="https://httpstat.us/503"} = [value]
sample_external_url_up{url="https://httpstat.us/200"} = 1
sample_external_url_response_ms{url="https://httpstat.us/200"} = [value]
```

### Looking for

- Good readme providing instructions what are the steps to run the python app in a k8s cluster.
- Dockerfile to build image.
- Helm chart to deploy this container on Kubernetes.
- Hint: use helm create
- Hint: Use Python prometheus-client module
