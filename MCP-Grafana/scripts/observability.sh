#!/bin/bash

NAMESPACE=grafana

echo "---------------------------------------------"
echo "🔹 Adding Helm Repositories"
echo "---------------------------------------------"

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add grafana https://grafana.github.io/helm-charts

# Create namespace if not exists
echo "---------------------------------------------"
echo "🔹 Ensuring Namespace Exists"
echo "---------------------------------------------"
kubectl get namespace "$NAMESPACE" >/dev/null 2>&1 || \
  kubectl create namespace "$NAMESPACE"

echo "---------------------------------------------"
echo "🔹 Installing Prometheus"
echo "---------------------------------------------"

helm upgrade --install my-prometheus prometheus-community/prometheus \
  --set server.service.type=NodePort \
  --set alertmanager.service.type=NodePort \
  --set nodeExporter.enabled=false \
  -n $NAMESPACE

echo "---------------------------------------------"
echo "🔹 Creating Grafana values.yaml"
echo "---------------------------------------------"

cat <<EOF > grafana-values.yaml
adminUser: admin
adminPassword: admin123

service:
  type: NodePort
  port: 80
  nodePort: 30093

datasources:
  datasources.yaml:
    apiVersion: 1
    datasources:
      - name: Prometheus
        type: prometheus
        access: proxy
        url: http://my-prometheus-server.${NAMESPACE}.svc.cluster.local
        isDefault: true
EOF

echo "---------------------------------------------"
echo "🔹 Installing Grafana"
echo "---------------------------------------------"



helm upgrade --install my-grafana-new grafana/grafana \
  -f grafana-values.yaml \
  -n $NAMESPACE

echo "---------------------------------------------"
echo "🎉 Installation Completed!"
echo "---------------------------------------------"

PROM_NODE_PORT=$(kubectl get svc my-prometheus-server -n $NAMESPACE -o jsonpath='{.spec.ports[0].nodePort}')
GRAFANA_NODE_PORT=$(kubectl get svc my-grafana-new -n $NAMESPACE -o jsonpath='{.spec.ports[0].nodePort}')

echo ""
echo "--------------------------------------------------"
echo "✔ Prometheus UI:"
echo "   👉 http://localhost:$PROM_NODE_PORT"
echo ""
echo "✔ Grafana UI:"
echo "   👉 http://localhost:$GRAFANA_NODE_PORT"
echo "   Username: admin"
echo "   Password: admin123"
echo "--------------------------------------------------"