# Jenkins

## Jenkins tutorials

[Installing jenkins on Linux (jenkins documentation)](https://www.jenkins.io/doc/book/installing/linux/#debianubuntu)

[How to Install Jenkins on Ubuntu 22.04](https://phoenixnap.com/kb/install-jenkins-ubuntu)

https://devopscube.com/configure-ssl-jenkins/

[Installing Jenkins with Let’s Encrypt certificate using Ansible](https://medium.com/@eriklotin/installing-jenkins-with-lets-encrypt-certificate-using-ansible-b077a6daa2a2)

[Cost Optimize your Jenkins CI/CD pipelines using EC2 Spot Instances](https://aws.amazon.com/fr/blogs/compute/cost-optimize-your-jenkins-ci-cd-pipelines-using-ec2-spot-instances/)

## Jenkins installation

### Prerequisites

- A system running Ubuntu 22.04 Jammy Jellyfish.
- A user account with administrator privileges.
- Access to a terminal window / command line (CTRL+ALT+T).
- Java 8 or 11 installed on Ubuntu.

### Steps

1. Download and install the necessary GPG key with the command 
   wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
   
2. Add the necessary repository with the command 
   sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
   
3. Add the universe repository with the command 
   sudo add-apt-repository universe
   
4. Update apt with the command 
   sudo apt-get update
   
5. Install Jenkins with the command 
   sudo apt-get install jenkins -y.
6. Allow the installation to complete.

See the ansible role for details.

## Usage

In the past I have used free style jenkins projects eventually group together an invoked from a jenkins pipeline.

As I want this project to follow the configuration as code principle, better to migrate to jenkins pipelines managed under source code management.

## Pipeline syntax differences
Declarative pipelines always begin with the word pipeline. Scripted pipelines, on the other hand, always begin with the word node. Declarative pipelines break down stages into individual stages that can contain multiple steps. Scripted pipelines use Groovy code and references to the Jenkins pipeline DSL within the stage elements without the need for steps.

Declarative syntax is recommended over scripted pipeline because scripting logic can make the pipelines complicated and hard to debug. If complicated things have to happen, encapsulate them into a jenkins plugin, a makefile, an ant or phing scripts, etc. 

## Pipeline edition

In the pipeline job configure page, there is a link to the pipeline documentation that contains a snippet generator.

   http://ratus.flub78.net:8080/job/M_pipeline/pipeline-syntax/

# Jenkins jobs

## Static analysis

- fetch the sources
- run the static analyzer
- publish the results

## phpunit for Laraval projects

This job is a little trickier as there is more pre-conditions and prerequisites.


