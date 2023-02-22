export aws_jenkins=ec2-13-37-229-138.eu-west-3.compute.amazonaws.com

# (Europe Paris = eu)
export AWS_DEFAULT_REGION=eu-west-3

# export BASENAME=ratus
# jsom, yaml, yaml-stream, text, table
# export AWS_DEFAULT_OUTPUT=text

export ANSIBLE_VAULT_PASSWORD_FILE=~/.ssh/ansible_vault_key

# Path: setenv.sh
export PATH=~/aws_cicd/python:$PATH

# Terrafom variables
export TF_VAR_PUBLIC_KEY="$HOME/.ssh/terraform.pub"
export TF_VAR_PRIVATE_KEY="$HOME/.ssh/terraform"

export PLAYBOOK=~/aws_cicd/ansible
