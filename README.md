# Containerized Simple Flask API

This application contains of 2 services, backend and frontend that each of service is running on a docker container in Kubernetes. Backend service will request the trivia from the [Numbers API](http://numbersapi.com), return the trivia via REST API based on current date. Frontend service will request the trivia to the backend and display it. Frontend service will runs publicly, meanwhile backend service is private so only frontend service can access the backend.
