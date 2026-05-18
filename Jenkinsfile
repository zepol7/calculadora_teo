pipeline {
    agent any

    environment {
        PROYECTO  = 'calculadora-demo'
        PYTHON_CMD = 'C:\\Users\\helio.lopez_davinci\\AppData\\Local\\Python\\bin\\python.exe'
        COBERTURA = '75'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
                bat '"C:\\Users\\helio.lopez_davinci\\AppData\\Local\\Python\\bin\\python.exe" --version'
                bat '"C:\\Users\\helio.lopez_davinci\\AppData\\Local\\Python\\bin\\python.exe" -m pip --version'
            }
        }

        stage('Instalar dependencias') {
            steps {
                bat '"C:\\Users\\helio.lopez_davinci\\AppData\\Local\\Python\\bin\\python.exe" -m pip install -r requirements.txt --quiet'
                bat '"C:\\Users\\helio.lopez_davinci\\AppData\\Local\\Python\\bin\\python.exe" -m pip install pytest pytest-cov flake8 --quiet'
                bat 'mkdir reports 2>nul || echo Carpeta ya existe'
            }
        }

        stage('Analisis estatico') {
            steps {
                bat '"C:\\Users\\helio.lopez_davinci\\AppData\\Local\\Python\\bin\\python.exe" -m flake8 src\\ test\\ --max-line-length=100 --statistics --count'
            }
        }

        stage('Pruebas unitarias') {
            steps {
                bat """
                    "C:\\Users\\helio.lopez_davinci\\AppData\\Local\\Python\\bin\\python.exe" -m pytest tests\\ -v ^
                      --tb=short ^
                      --junitxml=reports\\junit.xml ^
                      --cov=src ^
                      --cov-report=xml:reports\\coverage.xml ^
                      --cov-report=html:reports\\htmlcov ^
                      --cov-report=term-missing ^
                      --cov-fail-under=%COBERTURA%
                """
            }
            post {
                always {
                    junit 'reports\\junit.xml'
                    publishHTML(target: [
                        allowMissing         : false,
                        alwaysLinkToLastBuild: true,
                        keepAll              : true,
                        reportDir            : 'reports\\htmlcov',
                        reportFiles          : 'index.html',
                        reportName           : 'Cobertura de Codigo'
                    ])
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline EXITOSO — Proyecto: ${env.PROYECTO}"
        }
        failure {
            echo "Pipeline FALLIDO — Revisar los reportes"
        }
        always {
            cleanWs()
        }
    }
}