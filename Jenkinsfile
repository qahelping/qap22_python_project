pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                    python --version
                    python -m venv .venv
                    . .venv/bin/activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                    . .venv/bin/activate
                    mkdir -p reports
                    pytest tests/test_jenkins.py -v --junitxml=reports/results.xml
                '''
            }
        }
    }

    post {
        always {
            junit 'reports/results.xml'
        }
    }
}
