# Jenkins

## Jenkins tutorials

[Installing jenkins on Linux (jenkins documentation)](https://www.jenkins.io/doc/book/installing/linux/#debianubuntu)

[How to Install Jenkins on Ubuntu 22.04](https://phoenixnap.com/kb/install-jenkins-ubuntu)

[Installing Jenkins with Let’s Encrypt certificate using Ansible](https://medium.com/@eriklotin/installing-jenkins-with-lets-encrypt-certificate-using-ansible-b077a6daa2a2)

[DevOps CICD Pipeline with Ansible, Jenkins, GitHub & AWS](https://varunmanik1.medium.com/devops-cicd-pipeline-with-ansible-jenkins-github-aws-759e0440d51e)

[Setting up a CI/CD pipeline by integrating Jenkins with AWS CodeBuild and AWS CodeDeploy](https://aws.amazon.com/fr/getting-started/hands-on/setup-jenkins-build-server/)

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