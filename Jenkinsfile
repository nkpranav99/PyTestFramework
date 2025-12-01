pipeline {
  agent any

  // Optional parameter if you want to pass a selector (e.g. -k "smoke" or --browser chrome)
  parameters {
    string(name: 'browser_name', defaultValue: '', description: 'Optional pytest arg or selector (leave empty if not used)')
  }

  environment {
    VENV = ".venv"
    REPORTS = "jenkins_reports"
    // If your project needs a specific Python binary on some agents, change this to 'python' or detect in shell.
    PYTHON_BIN = "python3"
  }

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Setup Environment') {
      steps {
        sh '''
          set -e
          # create venv
          ${PYTHON_BIN} -m venv ${VENV}
          . ${VENV}/bin/activate

          # upgrade packaging tools
          python -m pip install --upgrade pip setuptools wheel

          # install poetry into the venv
          pip install poetry

          # Use poetry to install dependencies INCLUDING dev (so pytest is available).
          # If you intentionally want to skip dev deps, change to "poetry install --no-dev"
          poetry config virtualenvs.create false --local
          poetry install

          mkdir -p ${REPORTS}
        '''
      }
    }

    stage('Test') {
      steps {
        sh '''
          set -e
          . ${VENV}/bin/activate

          # Build pytest command. If browser_name param is empty, just run pytest.
          if [ -z "${browser_name}" ]; then
            pytest --junitxml=${REPORTS}/results.xml --maxfail=1 || true
          else
            # If browser_name is used to pass an actual pytest arg (like -k or -m or a custom flag),
            # ensure you pass it correctly when triggering the build.
            pytest ${browser_name} --junitxml=${REPORTS}/results.xml --maxfail=1 || true
          fi
        '''
      }
    }

    stage('Publish') {
      steps {
        // publish junit results (so Jenkins shows test report)
        junit allowEmptyResults: true, testResults: "${REPORTS}/results.xml"

        // archive the raw xmls and any logs you want to keep
        archiveArtifacts artifacts: "${REPORTS}/*", allowEmptyArchive: true
      }
    }
  }

  post {
    always {
      // best-effort cleanup
      sh 'rm -rf ${VENV} || true'
      cleanWs()
    }
    success { echo 'Pipeline completed successfully' }
    failure { echo 'Pipeline failed — check test results and console output' }
  }
}