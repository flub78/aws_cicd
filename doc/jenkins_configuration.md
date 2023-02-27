# Jenkins Configuration

Jenkins should be configured with no GUI or user interaction. It should follow the configuration as code principles.

The required configuration steps are:
- Creating a jenkins user
- adding the required jenkins modules
- creating the jenkins jobs.

I am not sure yet of the best way to put that in place. I had some trouble with the ansible jenkins_job module. The Jenkins configuration as code plugin is not perfectly trivial and cannot install modules. So there is still work to do to be able to get a fully automated jenkins configuration

## Jenkins user creation

Currently done manually once jenkins is installed. A token has also been created using the GUI to use the jenkins CLI tool.

TODO: automate jenkins user creation

TODO: automate jenkins user token creation

## Jenkins CLI tools

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


