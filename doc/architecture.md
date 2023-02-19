# Typical infrastructure

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

## Infrastructure description

### Terraform infrastucture provisioning

The infras/jenkins terraform configuration generates
- a key pair for ssh access
- a security groups with usual ports open
- an initial python web server
- an alarm to shut down unloaded instances
- a route to access the EC2 instance with a domain name

- a hosts file (ansible inventory)


## Ansible Roles

- test_connection.yml 

