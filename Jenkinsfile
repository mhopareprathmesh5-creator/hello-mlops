pipeline {
    agent any
    stages {
        stage('Checkout')    { steps { checkout scm } }
        stage('Build Image') { steps { bat 'docker build -t hello-mlops .' } }
        stage('Test')        { steps { bat 'docker run --rm hello-mlops python -m pytest -v -s' } }
        stage('Run App')     { steps { bat 'docker run --rm hello-mlops' } }
    }
}