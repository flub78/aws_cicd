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

### Jenkins server

It is an EC2 instance with 
- an apache server
- an elastic IP address
- a domain and a route S3 to connect the domain name to the EC2 instance

The apache server can be tested with http://[[domain]]
