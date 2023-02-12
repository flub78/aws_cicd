# Tools

In the context of personnal projects it is more important to have a fully automated CI/CD than to use the latest and greatest tools to implement it. Avoiding to long learning curve is important for individual and small teams.

The technologies chosen for that are:
* AWS to deploy virtual machines and virtual networks
* Terraform to provision the infrastructure
* Python 3 and boto3 to manage AWS object
* Ansible to populate the virtual machines
* Jenkins as automation server https://www.jenkins.io/
* github to manage the code and scripts

These tools make sense in 2023 for simple personnal projects. They could be replaced in the futur by more convenient ones, it is the CI/CD spirit which is important, not the tools.
