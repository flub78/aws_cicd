# My CICD pipeline

This is a description of the final objective and the description of the current state. Maybe that some technical choices are still motivated by my lack of expertize on some of the tools. 

I want:

1. An infrastructure to run the unit and end to end test on my current developments.

1. to destroy and recreate these pipeline easily. I have used Jenkins manually for years but every new deployment takes days of manual work.

1. Full automation, however I can accept to not have everything done at once. For example having to supply the jenkins initial password is temporary acceptable. 

I prefer:

1. A declarative over imperative approach. However after some difficulties to script the jenkins module installation I found that the easiest and more reliable one is to use Jenkins CLI.

The current idea is:
- To have a directory per infrastructure that I want to deploy and set everything from there.
- To have some shells script to setup the environment variables for the infrastructure. Once the environment is setup every command should automatically apply to the current environment.
- To deploy all the AWS objects using Terraform.
- To install the required software using Ansible
- To install jenkins modules using the Jenkins CLI.
- To manage Jenkins jobs in Jenkinsfile and manage them in each project SCM.

I like the Terraform approach to describe an infrastructure in a set of configuration files. Unfortunately in my approach the infrastructure also depends on what ansible playbooks have been applied. 

## Vaults and secrets

- All secretes and credentials should be kept outside of the SCM (or managed encrypted).

- Ansible secrets are stored and used encrypted in vaults. The password to access these vaults is kept in a file referenced by the ANSIBLE_VAULT_PASSWORD_FILE environment variable.

The ssh key installed by terraform to ssh in the EC2 instances is managed under my .ssh directory.

Terraform uses the AWS CLI credential to access to my AWS account.

So Terraform does not manages secret information.

Every other secrets should be managed by ansible inside a vault. It includes the laravel configuration files which contains database credentials.

## Example of infrastructure

The minimal set of servers that I want to deploy is:

- a Jenkins CI server
	- Static Analysis
	- Unit tests (maybe better to deploy that on another node ?)
	- Browser Controlled tests (same remark)
		
- Application servers
	- Test server
		- End to End tests
		- Deployment tests
	- Pre-production
		- Periodic import of the production data
		- Test of application migration
	- Production

## Who is in charge, Terraform, Ansible or Jenkins ?

Current status:

- The full creation of the infrastructure is done through successive invocation of Terraform scripts and Ansible scripts.

- Jenkins modules are currently installed from the jenkins CLI tool.

- Jenkins pipelines are created manually even if they reference a Jenkinsfile under SCM. 

- Some Jenkins jobs may invoke Ansible again. Should they also provision the AWS infrastructure to run the tests ?

It makes sense to have Jenkins reacting to code source changes and triggering from them the whole pipeline to test and validate. Should Jenkins rely on a static architecture with existing AWS instances or create them on the fly ?

TODO: fully automate pipelines creation.



## [Terraform infrastucture provisioning](terraform.md)

## [Ansible Playbooks and Roles](ansible.md)

## [Jenkins Configuration](jenkins_configuration.md)

## [Testing of the pipeline](Testing_roles.md)