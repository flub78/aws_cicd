# Introduction

## Typical deployment.

The first project to be integrated will be a continuous test and integration environment for a PHP Laravel project. This setup should be usable on others type of project just by changing the environment variables and the list of steps to perform.

## The control machine

It is the machine on which this git project is checked out and the scripts to create the CI/CD pipeline are executed.

It is important to have the minimal set of requirements on this machine. Typically I may want a Linux shell, may be an ansible or aws CLI environment but nothing more. In particular the setting of this machine must be really simple compared to the setting of the deployed pipeline.

If possible it should work on old Linux machine or limited environments like Raspberry PI or Windows WSL.


# Architecture

## Definitions

* Deployment: it is the set of all ressources required to provide one or several services. It may contain virtual networks, security keys, ec2 instances, etc. Two deployments may belong to different organization and they should not share resources.
* Deployment sub-system, it is the set or resources used to provide a service inside a deployment. For example a jenkins server, a test server or a production system. A subsystem can have dependencies or knowledge about other sub-systems. For example a jenkins server can interact with a virtual machine under test. Inside a deployment sub-systems can share resources, for example they can be inside the same VPC.
* Deployment components are the basic block of deployment or sub-system.

## Conventions

It may be convenient to apply the following naming convention:

* deployment: strings without dashes
* subs-systems: DeploymentName-SubSystemName (two strings dash separated)
* components: DeploymentName-SubSystem-Component or DeploymentName-Component (depending if the component is specific to a subsystem or not). To only have one format, it is possible to define a subsystem named "global".

It may also be convenient to add a string to define the type of the ID like, keypair, vpc, ec2instance, etc... (to be checked but it looks that AWS already enforce that sg-0b864f5c5c2ceb714, vpc-b615dbdf)

Note that this convention is only an option, it is possible to let the scripts create resources and use the random IDs returned by AWS but it will make the debugging and manual checking of the deployments much harder.

## Cost considerations

AWS bills you on the number of resources that you use and create. To optimize the costs, it may make sense to share some resources (for example to have only one virutal network for a team). So the scripts must be able to create all the components of a deployment but also to reuse existing one.

## Possible actions

The scripts must be able to create, run, restart, suspend or delete a deployment, a sub-system or a component.
* Create should create the create the required components
* Run should pass all component in active state
* Suspend or pause, should put them in a state that minimize billing
* Delete should erase the components for good. Note that pre-existing components should not be deleted. A full set of scripts should contains scripts to manage components and sub-systems. Every script should be in charge of a sub-system or component and should be the only way to create or delete the resources (just to avoid side effect of components deleted by a script which has not created them).

So the scripts should all have the same structrure:

    script_level type action id options
    script_level = dep, sub or comp for deployment, sub-system or component

    type:
        * for deployment describe the type of deployments that the scripts can handle example, the name of a laravel project, or an android project, etc.
        * for the subsystem, it identifies the type of subsystem, for example test_server, jenkins server, production env, etc.
        * for components, it identifies the type of component, vpc, ec2, key_pair, etc.

    actions: create, run, suspend, delete, list, ect.

    ID : ID of the entity to create or handle, optional for some commands like list.

    Options may describe some share resources or others options.

* dep type create id
* sub 


