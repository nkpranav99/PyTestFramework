pipeline {
    agent any

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
                export PIP_CACHE="${WORKSPACE}/.cache/pip"
                export REPORT_DIR="${WORKSPACE}/test-reports"
                export ARTIFACT_DIR="${WORKSPACE}/artifacts"
                mkdir -p ${PIP_CACHE} ${REPORT_DIR} ${ARTIFACT_DIR}

                if [ ! -d "${VENV_DIR}" ]; then
                    python -m venv "${VENV_DIR}"
                fi

                "${VENV_DIR}/bin/python" -m pip install --upgrade pip setuptools wheel

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