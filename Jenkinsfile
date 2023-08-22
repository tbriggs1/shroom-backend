pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = "shroom-api:${GIT_BRANCH}"
        DOCKER_REPO = "tombriggs/shroom-api"
        DOCKER_TAG = "${DOCKER_REPO}:${BRANCH_NAME}"
    }
    stages {
        stage('Build') {
            steps {
                echo "Building branch: ${BRANCH_NAME}"

                sh "docker build . -t ${DOCKER_IMAGE_NAME}"
                sh "docker tag ${DOCKER_IMAGE_NAME} ${DOCKER_TAG}"
                sh "docker push ${DOCKER_TAG}"
            }
        }
        stage('Deploy'){
            steps {
                sh "docker run -d -p 8000:8000 ${DOCKER_IMAGE_NAME}"
            }
        }
    }
}