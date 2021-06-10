pipeline {
    agent any
    environment {
        DOCKER_USERNAME = credentials('DOCKER_USERNAME')
        DOCKER_PASSWORD = credentials('DOCKER_PASSWORD')
    }
    stages {
        stage('Install Requirements') {
            steps {
                sh 'bash scripts/install-requirements.sh'
            }
        }

        stage('Test') {
            steps {
                //pytest
                //run for each service
                //produce cov reports
                sh 'bash scripts/test.sh'
            }
        }
        stage('Build') {
            steps {
                //install docker and docker compose
                //docker-compose build
                sh 'docker-compose build'
            }
        }
        stage('Push') {
            steps{
                //install docker and docker compose
                //docker-compose build
                sh 'docker-compose push'
            }
        }
        stage('Configuration Management (Ansible)') {
            steps {
                //install ansible on jenkins machine for the Jenkins user
                //ansible-playbook -i inventory.yaml playbook.yaml
                sh 'echo config'
            }
        }
        stage('Deploy') {
            steps{
                //create swarm infrastructure
                //copy over docker-compose.yaml
                //ssh: docker stack deploy --compose-file docker-compose.yaml animal_noises
                sh 'echo deploy'
            }
        }
    }
}