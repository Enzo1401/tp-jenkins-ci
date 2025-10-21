pipeline {
    agent any

    options {
        // Ajoute les horodatages aux logs
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                // Active les couleurs ANSI pour cette étape
                ansiColor('xterm') {
                    // Récupération du code source
                    checkout scm
                }
            }
        }

        stage('Setup Python venv') {
            steps {
                ansiColor('xterm') {
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
        }

        stage('Tests') {
            steps {
                ansiColor('xterm') {
                    sh '''
                        set -e
                        . venv/bin/activate
                        # Si vous utilisez pytest :
                        # python -m pip install pytest
                        # pytest -q
                        # Ici on utilise unittest (intégré) :
                        python -m unittest -v
                    '''
                }
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
