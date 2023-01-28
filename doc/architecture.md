# CI/CD architecture

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

## CI/CD use cases

I need scripts and command to

- create, list and delete an infrastructure or its components
- suspend and resume the infrastructure (to control the costs)
- create a jenkins server and add plugins
- install a job in the jenkins server
- deploy an application