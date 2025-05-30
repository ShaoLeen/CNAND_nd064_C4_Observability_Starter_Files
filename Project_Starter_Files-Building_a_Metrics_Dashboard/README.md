**Note:** All referenced screenshots are in the `answer-img` directory.

## Verify the monitoring installation

*TODO:* run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation

kubectl all pods.png
kubectl all services.png

## Setup the Jaeger and Prometheus source
*TODO:* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.

Grafana initial login.png

## Create a Basic Dashboard
*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.

Grafana - Prometheus dashboard.png

## Describe SLO/SLI
*TODO:* Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.

At first !availability! showing the total number of (HTTP) requests and their responses over a timespan of a month.
Secondly the !latency! showing the request response time.

## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs. 
1. SLI: Uptime success rate => http total requests shall show the incoming requests, which are resulting in successful responses.
2. SLI: Response Time => http request duration shall show the latency in handling http requests, ideally with a treshold of under <300ms.
3. SLI: Uptime probes => This shall show if the service endpoints are reachable and returning expected responses.
4. SLI: Error rates => http total requests shall also show http errors (4xx and 5xx status codes).
5. SLI: System load => Base components like CPU and memory shall be shown to have a pro-active view on the actual load and potential spikes. 

## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.

Dashboard has been uploaded by the name "uptime 4xx 5xx - SLI dashboard.png".
Used metrics are shown below the separated panels.
Uptime measurement is combined for backend- and frontend-serice implying all pods.

## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here. Also provide a (screenshot) sample Python file containing a trace and span code used to perform Jaeger traces on the backend service.

The filled span with a test endpoint is shown in "Jaeger test span filled.png".
The full backend Python code is shown in "full backend code including tracing and test span endpoint.png".

## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.

The Jaeger test span from above for the backend-service is shown in "Grafana panel - Jaeger test span.png" in one Grafana panel.

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue also include a screenshot of the tracer span to demonstrate how we can user a tracer to locate errors easily.

TROUBLE TICKET

Name: broken endpoint on backend-service

Date: 08.05.2025

Subject: HTTP 500 

Affected Area: backend-service

Severity: low

Description: The backend-app is monitored throug a service monitor related to backend-service seen in Jaeger and Grafana. While accessing the /error endpoint the backend-service is bringing up a HTTP 500 error as shown in the "simulated troubleticket error.png". 


## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name four SLIs that you would use to measure the success of this SLO.

1. Uptime of frontend and backend
2. HTTP 2xx success rate
3. HTTP 5xx errors
4. Latency of frontend

## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create a list of 2-3 KPIs to accurately measure these metrics as well as a description of why those KPIs were chosen. We will make a dashboard for this, but first write them down here.

1. The frontend latency has to be lower than 100ms. => Higher latency means higher drop rate by users, resulting in less acceptance of the service.
2. The HTTP 2xx success rate needs to be at least 99,95% per month. => The success rate shall cover the availability aspect of the service in addition to the plain uptime. 
3. The uptime of frontend and backend needs to be at least 99,95% per month. => Essential SLI for having an overview of the overall uptime of the frontend and backend. 

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  

The dashboard is shown in "Final dashboard.png" containing the following panels:
1. The frontend latency is shown on a 99,95% percentile over a 30 days period of time.
2. HTTP 2xx success rate is shown as percentage over a 30 days period of time.
3. The uptime status of frontend and backend (all pods) are shown over a period of 30days. 
