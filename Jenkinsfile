pipeline {
    agent any

    environment {
        PIP_CACHE = "/root/.cache/pip"
        REPORT_DIR = "${env.WORKSPACE}/test-reports"
        ARTIFACT_DIR = "${env.WORKSPACE}/artifacts"
    }

    stages {
        stage("Checkout Project") {
            steps{
                checkout scm
            }
        }
        stage("Setup Environment for Tests") {
            agent {
                docker {
                    image 'python:3.11-slim'
                }
            }
            steps {
                sh '''
                set -e
                echo "Python: $(python --version)"
                mkdir -p ${PIP_CACHE} ${REPORT_DIR} ${ARTIFACT_DIR}
                python -m pip install --upgrade pip setuptools wheel
                if [ -f requirements.txt ]; then
                    python -m pip install --cache-dir=${PIP_CACHE} -r requirements.txt
                else
                    echo "No requirements.txt found; skipping dependency install"
                fi
                '''
            }
        }
        stage('Run Tests (Docker)') {
            agent {
                docker {
                image 'python:3.11-slim'
                // args: '-v /host/path/.pip_cache:/root/.cache/pip' // keep cache consistent if mounted above
                }
            }
            steps {
                sh '''
                set -e
                mkdir -p ${REPORT_DIR}
                # run tests and write junit xml
                python -m pytest -q --junitxml=${REPORT_DIR}/junit.xml || true
                '''
            }
            post {
                always {
                junit allowEmptyResults: true, testResults: '${WORKSPACE}/test-reports/junit.xml'
                archiveArtifacts artifacts: 'test-reports/**/*', allowEmptyArchive: true
                }
            }
        }

    }
    post {
        success { echo "Pipeline succeeded" }
        unstable { echo "Pipeline finished — some tests failed (unstable)" }
        failure { echo "Pipeline failed" }
    }
}