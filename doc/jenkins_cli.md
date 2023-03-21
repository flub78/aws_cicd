# Jenkins CLI

## Installation

On the jenkins server : http://jenkins.domain:8080/manage/cli/

* Download the jar file, wget ...

```sh
~/jenkins-cli$ java -jar jenkins-cli.jar -s http://jenkins.flub78.net:8080/  who-am-i
Authenticated as: anonymous
Authorities:
  anonymous
```

```sh
~/jenkins-cli$ java -jar jenkins-cli.jar -s http://jenkins.flub78.net:8080/  -auth jenkins:xxxxxxxxxxxxx who-am-i
Authenticated as: jenkins
Authorities:
  authenticated
```

To install a plugin:
```sh
~/jenkins-cli$ java -jar jenkins-cli.jar -s http://jenkins.flub78.net:8080/  -auth jenkins:xxxxxxxxxxxxxxx install-plugin pipeline-utility-steps
Installing pipeline-utility-steps from update center
```

## Create an API token

Once connected chose configure on the user context menu.


Jeton d'API (token)

Add the token to a file with the format user:token

alias jcli='java -jar jenkins-cli.jar -s http://jenkins.flub78.net:8080/ -auth @jenkins_token'

```
~/jenkins-cli$ jcli who-am-i
Authenticated as: jenkins
Authorities:
  authenticated
```
