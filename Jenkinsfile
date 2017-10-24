pipeline {
    agent any
    options {
        timeout(time: 1, unit: 'HOURS') 
    }
    triggers {
        pollSCM('1 * * * *')
    }
    stages {
        stage('Unit Testing') {
            steps {
                parallel(
                    "Front-End Tests": {
                        echo 'Hello front-end!'
                        sh 'run_travis.sh frontend'
                    },
                    "Back-End Tests": {
                        sh 'run_travis.sh backend'
                    },
                    "Acceptance Tests": {
                        echo 'Hello acceptance!'
                        sh 'run_travis.sh acceptance'
                    }
                )
            }
        }
        stage('Coverage') {
            steps {
                parallel(
                    "Front-End Coverage": {
                        sleep 1
                        echo 'Hello front-end coverage!'
                    },
                    "Back-End Coverage": {
                        sleep 1
                        echo 'Hello back-end coverage!'
                    }
                )
            }
        }
    }
}
