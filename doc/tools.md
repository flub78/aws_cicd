# Tools

There is always a tradeof about tools selection between efficiency and learning curve. It makes sense for a big organization to invest in training on the most powerful tools. They have engineers who are spending most of their time on DevOps and even small gains in productivity can save a lot of time. For personnal projects and small team the time to get familiar with and select sophisticated tools is directly substracted from the development capacity. Of course not automating the test and deployment also have big negative impact on small projects, even to the point of having to freeze a project because of lack of time to test the project and track regression. 

In the context of personnal projects it is more important to have a fully automated CI/CD than to use the latest and greatest tools to get it.

The technologies chosen for that are:
* AWS to deploy virtual machines and virtual networks
* Python 3 and boto3 to manage AWS object
* ansible to populate the virtual machines
* jenkins as automation server https://www.jenkins.io/
* github to manage the code and scripts

Of course these tools make sense in 2023, but maybe that they will be replaced in the futur by more convenient ones. It is the CI/CD spirit which is important, not the tools.