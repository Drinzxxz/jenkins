pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git credentialsId: 'github-token', url: 'https://github.com/Drinzxxz/jenkins.git', branch: 'main'
            }
        }
    }
}
