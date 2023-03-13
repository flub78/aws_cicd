# infras directory

This directory contains one subdirectory per block of infrastructure.

The jenkins infrastructure must be deployed first as it creates some resources referenced by other elements.

**Warning the terraform temporary data must not be saved in github, put them in .gitignore** 