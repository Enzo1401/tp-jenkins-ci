pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                // Récupération du code source depuis GitHub
                checkout scm
            }
        }

        stage('Setup Python venv') {
            steps {
                sh '''
                    set -e
                    if ! command -v python3 >/dev/null 2>&1; then
                        echo "Python3 manquant sur l'agent Jenkins. Installez Python 3.10+."
                        exit 1
                    fi
                    python3 -m venv venv
                    . venv/bin/activate
                    python -m pip install --upgrade pip
                '''
            }
        }

        stage('Tests') {
            steps {
                sh '''
                    set -e
                    . venv/bin/activate
                    python -m unittest -v
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/*.py', onlyIfSuccessful: false
        }
        success {
            echo '✅ Pipeline OK'
        }
        failure {
            echo '❌ Pipeline en échec — vérifiez les logs de la stage "Tests"'
        }
    }
}
