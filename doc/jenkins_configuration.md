# Jenkins Configuration

This part is still a job in progress. I am experimenting miscellaneous solution of jenkins configuration "as code".

Jenkins should be configured with no GUI or user interactions.

The required configuration steps are:
- Creating a jenkins user
- adding the required jenkins modules
- creating the jenkins jobs.

I have some trouble with the ansible jenkins_job module. The Jenkins configuration as code plugin is not as trivial than presented and cannot install jenkins modules. I am looking for a simple solution with low learning curve and have a preference for DSL approach compared to XML edition or a complex API. If possible I'd prefer a unique tool for jenkins configuration and job creation instead of mixing ansible jenkins cli and jenkins plugins.

## The Jenkins user creation

Currently done manually once jenkins is installed. A token has also been created using the GUI to use the jenkins CLI tool.

TODO: automate jenkins user creation

TODO: automate jenkins user token creation


## Installing Jenkins modules using Jenkins CLI

It is an easy to use tool:

[Jenkins CLI documentation](https://www.jenkins.io/doc/book/managing/cli/)

```sh
mkdir jenkins-cli
cd jenkins-cli/
wget http://ratus.flub78.net:8080/jnlpJars/jenkins-cli.jar

java -jar jenkins-cli.jar -s http://ratus.flub78.net:8080/ who-am-i
```

To do anything useful a token is required. It should be put in a file with the syntax user:TOKEN

basic commands:
```sh
java -jar jenkins-cli.jar -s http://ratus.flub78.net:8080/ -auth @jenkins_token who-am-i

java -jar jenkins-cli.jar -s http://ratus.flub78.net:8080/ -auth @jenkins_token install-plugin phing
java -jar jenkins-cli.jar -s http://ratus.flub78.net:8080/ -auth @jenkins_token install-plugin htmlpublisher
		
java -jar jenkins-cli.jar -s http://ratus.flub78.net:8080/ -auth @jenkins_token safe-restart
		
java -jar jenkins-cli.jar -s http://ratus.flub78.net:8080/ -auth @jenkins_token list-jobs
```
## Jenkinsfile

Jenkinsfiles are managed in the project that they test. That way the Jenkins jobs can be kept really simple and generic and the logic of the pipeline are managed under CSM.

## Agent Nodes

For security reasons and for more efficient resource management the jobs are executed on several agents.

Folowing this tutorial step by step I got it working

	https://docs.cloudbees.com/docs/cloudbees-ci-kb/latest/client-and-managed-masters/how-to-connect-to-remote-ssh-agents


## Others tools

### Configuration as code

pro: 
- look promising
- DSL approach

cons: My first attempt resulted on an error with an angry red jenkins and not a single explanation ...

### Ansible jenkins module

pro: 
look promising

cons: 
- XML editing for job creation

### Jenkins DSL job plugin

pro:
- based on DSL

cons:
- you have to bootstrap

## Jenkins CLI tools



