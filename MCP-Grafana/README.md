# Grafana MCP server

A [Model Context Protocol][mcp] (MCP) server for Grafana.

## Requirements

- **Grafana version 9.0 or later** is required for full functionality. Some features, particularly datasource-related operations, may not work correctly with earlier versions due to missing API endpoints.


### Dashboards

- **Search for dashboards:** Find dashboards by title or other metadata
- **Get dashboard by UID:** Retrieve full dashboard details using its unique identifier. _Warning: Large dashboards can consume significant context window space._
- **Get dashboard summary:** Get a compact overview of a dashboard including title, panel count, panel types, variables, and metadata without the full JSON to minimize context window usage
- **Get dashboard property:** Extract specific parts of a dashboard using JSONPath expressions (e.g., `$.title`, `$.panels[*].title`) to fetch only needed data and reduce context window consumption
- **Update or create a dashboard:** Modify existing dashboards or create new ones. _Warning: Requires full dashboard JSON which can consume large amounts of context window space._
- **Patch dashboard:** Apply specific changes to a dashboard without requiring the full JSON, significantly reducing context window usage for targeted modifications
- **Get panel queries and datasource info:** Get the title, query string, and datasource information (including UID and type, if available) from every panel in a dashboard


### Datasources

- **List and fetch datasource information:** View all configured datasources and retrieve detailed information about each.
  - _Supported datasource types: Prometheus, Loki._

### Prometheus Querying

- **Query Prometheus:** Execute PromQL queries (supports both instant and range metric queries) against Prometheus datasources.
- **Query Prometheus metadata:** Retrieve metric metadata, metric names, label names, and label values from Prometheus datasources.

### Loki Querying

- **Query Loki logs and metrics:** Run both log queries and metric queries using LogQL against Loki datasources.
- **Query Loki metadata:** Retrieve label names, label values, and stream statistics from Loki datasources.

### Incidents

- **Search, create, and update incidents:** Manage incidents in Grafana Incident, including searching, creating, and adding activities to incidents.

### Sift Investigations

- **List Sift investigations:** Retrieve a list of Sift investigations, with support for a limit parameter.
- **Get Sift investigation:** Retrieve details of a specific Sift investigation by its UUID.
- **Get Sift analyses:** Retrieve a specific analysis from a Sift investigation.
- **Find error patterns in logs:** Detect elevated error patterns in Loki logs using Sift.
- **Find slow requests:** Detect slow requests using Sift (Tempo).

### Alerting

- **List and fetch alert rule information:** View alert rules and their statuses (firing/normal/error/etc.) in Grafana.
- **List contact points:** View configured notification contact points in Grafana.

### Grafana OnCall

- **List and manage schedules:** View and manage on-call schedules in Grafana OnCall.
- **Get shift details:** Retrieve detailed information about specific on-call shifts.
- **Get current on-call users:** See which users are currently on call for a schedule.
- **List teams and users:** View all OnCall teams and users.
- **List alert groups:** View and filter alert groups from Grafana OnCall by various criteria including state, integration, labels, and time range.
- **Get alert group details:** Retrieve detailed information about a specific alert group by its 

#### RBAC Scopes

Scopes define the specific resources that permissions apply to. Each action requires both the appropriate permission and scope combination.


### Tools

| Tool                              | Category    | Description                                                        | Required RBAC Permissions               | Required Scopes                                     |
| --------------------------------- | ----------- | ------------------------------------------------------------------ | --------------------------------------- | --------------------------------------------------- |
| `list_teams`                      | Admin       | List all teams                                                     | `teams:read`                            | `teams:*` or `teams:id:1`                           |
| `list_users_by_org`               | Admin       | List all users in an organization                                  | `users:read`                            | `global.users:*` or `global.users:id:123`           |
| `search_dashboards`               | Search      | Search for dashboards                                              | `dashboards:read`                       | `dashboards:*` or `dashboards:uid:abc123`           |
| `get_dashboard_by_uid`            | Dashboard   | Get a dashboard by uid                                             | `dashboards:read`                       | `dashboards:uid:abc123`                             |
| `update_dashboard`                | Dashboard   | Update or create a new dashboard                                   | `dashboards:create`, `dashboards:write` | `dashboards:*`, `folders:*` or `folders:uid:xyz789` |
| `get_dashboard_panel_queries`     | Dashboard   | Get panel title, queries, datasource UID and type from a dashboard | `dashboards:read`                       | `dashboards:uid:abc123`                             |
| `get_dashboard_property`          | Dashboard   | Extract specific parts of a dashboard using JSONPath expressions   | `dashboards:read`                       | `dashboards:uid:abc123`                             |
| `get_dashboard_summary`           | Dashboard   | Get a compact summary of a dashboard without full JSON             | `dashboards:read`                       | `dashboards:uid:abc123`                             |
| `list_datasources`                | Datasources | List datasources                                                   | `datasources:read`                      | `datasources:*`                                     |
| `get_datasource_by_uid`           | Datasources | Get a datasource by uid                                            | `datasources:read`                      | `datasources:uid:prometheus-uid`                    |
| `get_datasource_by_name`          | Datasources | Get a datasource by name                                           | `datasources:read`                      | `datasources:*` or `datasources:uid:loki-uid`       |
| `query_prometheus`                | Prometheus  | Execute a query against a Prometheus datasource                    | `datasources:query`                     | `datasources:uid:prometheus-uid`                    |
| `list_prometheus_metric_metadata` | Prometheus  | List metric metadata                                               | `datasources:query`                     | `datasources:uid:prometheus-uid`                    |
| `list_prometheus_metric_names`    | Prometheus  | List available metric names                                        | `datasources:query`                     | `datasources:uid:prometheus-uid`                    |
| `list_prometheus_label_names`     | Prometheus  | List label names matching a selector                               | `datasources:query`                     | `datasources:uid:prometheus-uid`                    |
| `list_prometheus_label_values`    | Prometheus  | List values for a specific label                                   | `datasources:query`                     | `datasources:uid:prometheus-uid`                    |
| `list_incidents`                  | Incident    | List incidents in Grafana Incident                                 | Viewer role                             | N/A                                                 |
| `create_incident`                 | Incident    | Create an incident in Grafana Incident                             | Editor role                             | N/A                                                 |
| `add_activity_to_incident`        | Incident    | Add an activity item to an incident in Grafana Incident            | Editor role                             | N/A                                                 |
| `get_incident`                    | Incident    | Get a single incident by ID                                        | Viewer role                             | N/A                                                 |
| `query_loki_logs`                 | Loki        | Query and retrieve logs using LogQL (either log or metric queries) | `datasources:query`                     | `datasources:uid:loki-uid`                          |
| `list_loki_label_names`           | Loki        | List all available label names in logs                             | `datasources:query`                     | `datasources:uid:loki-uid`                          |
| `list_loki_label_values`          | Loki        | List values for a specific log label                               | `datasources:query`                     | `datasources:uid:loki-uid`                          |
| `query_loki_stats`                | Loki        | Get statistics about log streams                                   | `datasources:query`                     | `datasources:uid:loki-uid`                          |
| `list_alert_rules`                | Alerting    | List alert rules                                                   | `alert.rules:read`                      | `folders:*` or `folders:uid:alerts-folder`          |
| `get_alert_rule_by_uid`           | Alerting    | Get alert rule by UID                                              | `alert.rules:read`                      | `folders:uid:alerts-folder`                         |
| `list_contact_points`             | Alerting    | List notification contact points                                   | `alert.notifications:read`              | Global scope                                        |
| `list_oncall_schedules`           | OnCall      | List schedules from Grafana OnCall                                 | `grafana-oncall-app.schedules:read`     | Plugin-specific scopes                              |
| `get_oncall_shift`                | OnCall      | Get details for a specific OnCall shift                            | `grafana-oncall-app.schedules:read`     | Plugin-specific scopes                              |
| `get_current_oncall_users`        | OnCall      | Get users currently on-call for a specific schedule                | `grafana-oncall-app.schedules:read`     | Plugin-specific scopes                              |
| `list_oncall_teams`               | OnCall      | List teams from Grafana OnCall                                     | `grafana-oncall-app.user-settings:read` | Plugin-specific scopes                              |
| `list_oncall_users`               | OnCall      | List users from Grafana OnCall                                     | `grafana-oncall-app.user-settings:read` | Plugin-specific scopes                              |
| `list_alert_groups`               | OnCall      | List alert groups from Grafana OnCall with filtering options       | `grafana-oncall-app.alert-groups:read`  | Plugin-specific scopes                              |
| `get_alert_group`                 | OnCall      | Get a specific alert group from Grafana OnCall by its ID           | `grafana-oncall-app.alert-groups:read`  | Plugin-specific scopes                              |
| `get_sift_investigation`          | Sift        | Retrieve an existing Sift investigation by its UUID                | Viewer role                             | N/A                                                 |
| `get_sift_analysis`               | Sift        | Retrieve a specific analysis from a Sift investigation             | Viewer role                             | N/A                                                 |
| `list_sift_investigations`        | Sift        | Retrieve a list of Sift investigations with an optional limit      | Viewer role                             | N/A                                                 |
| `find_error_pattern_logs`         | Sift        | Finds elevated error patterns in Loki logs.                        | Editor role                             | N/A                                                 |
| `find_slow_requests`              | Sift        | Finds slow requests from the relevant tempo datasources.           | Editor role                             | N/A                                                 |
| `list_pyroscope_label_names`      | Pyroscope   | List label names matching a selector                               | `datasources:query`                     | `datasources:uid:pyroscope-uid`                     |
| `list_pyroscope_label_values`     | Pyroscope   | List label values matching a selector for a label name             | `datasources:query`                     | `datasources:uid:pyroscope-uid`                     |
| `list_pyroscope_profile_types`    | Pyroscope   | List available profile types                                       | `datasources:query`                     | `datasources:uid:pyroscope-uid`                     |
| `fetch_pyroscope_profile`         | Pyroscope   | Fetches a profile in DOT format for analysis                       | `datasources:query`                     | `datasources:uid:pyroscope-uid`                     |
| `get_assertions`                  | Asserts     | Get assertion summary for a given entity                           | Plugin-specific permissions             | Plugin-specific scopes                              |
| `generate_deeplink`               | Navigation  | Generate accurate deeplink URLs for Grafana resources              | None (read-only URL generation)         | N/A                                                 |

## CLI Flags Reference

The `mcp-grafana` binary supports various command-line flags for configuration:

**Transport Options:**
- `-t, --transport`: Transport type (`stdio`, `sse`, or `streamable-http`) - default: `stdio`
- `--address`: The host and port for SSE/streamable-http server - default: `localhost:8000`
- `--base-path`: Base path for the SSE/streamable-http server
- `--endpoint-path`: Endpoint path for the streamable-http server - default: `/`

**Debug and Logging:**
- `--debug`: Enable debug mode for detailed HTTP request/response logging

### How to Spin your own MCP Grafana
 
You have several options to install `mcp-grafana`:

1) git clone <REPO>
2) sh -x scripts/observability.sh  
3) kubectl get pods -n grafana -> Verify if all up and running
4) Open Grafana with endpoint you see after step2.

5) Open http://localhost:30093
Go to Administration -> Users and Access -> Service Account 
Get token <YOUR_TOKEN_HERE>

6) Run below commands to get MCP Server up locally from the Image you created

docker build -t mcp-grafana .
docker run -d -p 8000:8000 \
  -e GRAFANA_URL=http://host.docker.internal:30093 \
  -e GRAFANA_SERVICE_ACCOUNT_TOKEN=<TOKEN>\
  mcp-grafana \
  -t streamable-http

7) Verify MCP Server via Inspector by below command:
npx @modelcontextprotocol/inspector
* Check Browser and select correct Protocol and give URL as http://localhost:8000/mcp 
* List Tools
* Use `list_datasources` tool and enter "prometheus" as type. (eg DataSource UID PBFA97CFB590B2093)
* Use `search_dashboards` tool and enter and dahboard UID
* Use `query_prometheus` tool and enter DS and PROMQL :
UID: PBFA97CFB590B2093
expr: sum(rate(container_cpu_usage_seconds_total{namespace="grafana", pod!=""}[2m])) by (pod) * 100
endtime: now-10m
startime: now
