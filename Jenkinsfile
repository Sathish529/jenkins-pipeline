pipeline {
environment {
registry = "vinodh1988leo"
registryCredential = 'dockerCredentials'
dockerImage = 'flask-app-docker'
}
agent any
stages {
stage('Cloning our Git') {
steps {
git 'https://github.com/vinodh1988/sre-flask-app'
}
}
stage('Building our image') {
steps{
script {
dockerNow = docker.build registry+"/"+ dockerImage + ":$BUILD_NUMBER"
}
}
}
stage('Deploy our image') {
steps{
script {
docker.withRegistry( '', registryCredential ) {
dockerNow.push()
}
}
}
}
stage('Cleaning up') {
steps{
sh "docker rmi $registry/$dockerImage:$BUILD_NUMBER"
}
}
}
}