# Infrastructure description

The minimal set of servers that I want to deploy is:

- Jenkins CI server
	- Static Analysis
	- Unit tests
	- Browser Controlled tests
		
- Application servers
	- Test server
		- End to End tests
		- Deployment tests
	- Pre-production
		- Periodic import of the production data
		- Test of application migration
	- Production

## [Terraform infrastucture provisioning](terraform.md)

## [Ansible Playbooks and Roles](ansible.md)

## [Pipeline Testing](Testing_roles.md)