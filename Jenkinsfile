node('master') {
    stage("Fetch Source Code") {
        git 'https://github.com/kenoseni/jenkinswithflask'
    }
    
    printMessage('Running Pipeline')

    stage("Testing") {
        printMessage('We are about to start testing the app')
    }
    
    stage("Deployment") {
        if(env.BRANCH_NAME == 'master') {
            printMessage('Deploying to develop branch')
        }else {
            printMessage('No deployment configured for this branch')
        }
    }
        
    printMessage('Pipeline Complete')
}
def printMessage(message){
    echo "${message}"
}