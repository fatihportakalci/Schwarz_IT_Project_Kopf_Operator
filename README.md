# Schwarz_IT_Project_Kopf_Operator

Vorbereitung des Python-Skripts

1.Nutzung der  Dokumentation auf Kopf Startup Documentation zur Entwicklung des erforderlichen Python-Codes für den Operator
	- Speichern den Code in einer Datei kopf_operator.py


2.Erstellung Dockerfile im selben Verzeichnis wie  Python-Skript

FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["kopf", "run", "kopf_operator.py"]

Erstellung auch eine requirements.txt-Datei, die kopf und alle anderen benötigten Bibliotheken enthält.

3.Bauen Docker-Image

docker build -t fatihportakalci/schwarz-projekt:1.1 .

Lade Image auf Docker Hub hoch:

docker push fatihportakalci/schwarz-projekt:1.1

4. Erstellung deployment.yaml-Datei für das Deployment

apiVersion: apps/v1
kind: Deployment
metadata:
  name: kopf-operator
spec:
  replicas: 1
  selector:
    matchLabels:
      app: kopf-operator
  template:
    metadata:
      labels:
        app: kopf-operator
    spec:
      containers:
      - name: kopf-operator
        image: fatihportakalci/schwarz-projekt:1.1
        ports:
        - containerPort: 8080

5. Erstellung service.yaml-Datei für den Service:

apiVersion: v1
kind: Service
metadata:
  name: kopf-operator-service
spec:
  type: NodePort
  ports:
  - port: 8080
    targetPort: 8080
    nodePort: 30001
  selector:
    app: kopf-operator

6. Bereitstellung für das Kubernetes und Anwendung 

kubectl apply -f .

- Überprüfung der service.yaml und pods

kubectl get pods
kubectl get svc

7. Der Service kann jetzt über die IP eines der Knoten des Clusters zusammen mit dem NodePort (30001) erreicht werden

	- Verwendung des kubectl get nodes -o wide um die IP-Adressen der Knoten zu finden 

Finish





