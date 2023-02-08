> ># configure jenkins with https and lets-encrypt with systemd
> 
> Here are the steps to configure Jenkins with HTTPS and Let's Encrypt using Systemd:
> 
> 1.  Obtain a domain name: Before setting up HTTPS, you need a domain name that resolves to your server. You can purchase a domain name from various domain registrars such as GoDaddy, Namecheap, etc.
>     
> 2.  Install Let's Encrypt client: Install a Let's Encrypt client, such as certbot, on your server.
>     
> 3.  Obtain SSL certificate: Run the following command to obtain an SSL certificate:
>     
> 
> css
> 
> ```css
> sudo certbot certonly --standalone -d example.com
> ```
> 
> Replace "example.com" with your domain name.
> 
> 4.  Create Systemd service file: Create a Systemd service file for Jenkins, usually located at `/etc/systemd/system/jenkins.service`, and paste the following content:
> 
> css
> 
> ```css
> [Unit]
> Description=Jenkins Continuous Integration Server
> After=network.target
> 
> [Service]
> User=jenkins
> WorkingDirectory=/var/lib/jenkins
> ExecStart=/usr/bin/java -jar /usr/share/jenkins/jenkins.war --httpListenAddress=0.0.0.0 --httpPort=8080 --httpsPort=8443 --httpsCertificate=/etc/letsencrypt/live/example.com/fullchain.pem --httpsPrivateKey=/etc/letsencrypt/live/example.com/privkey.pem
> 
> [Install]
> WantedBy=multi-user.target
> ```
> 
> Replace "example.com" with your domain name.
> 
> 5.  Reload Systemd: Run the following command to reload Systemd:
> 
> `sudo systemctl daemon-reload`
> 
> 6.  Start and enable Jenkins: Run the following command to start and enable Jenkins:
> 
> bash
> 
> ```bash
> sudo systemctl start jenkins
> sudo systemctl enable jenkins
> ```
> 
> 7.  Test your configuration: Open a web browser and navigate to `https://example.com:8443`. You should see the Jenkins login page with a green padlock icon, indicating that the connection is secure.
> 
> Note: These steps are meant to be a general guide and may differ slightly depending on your system setup and configuration.
> 
># An ansible role to do that
> 
> Here's an example Ansible role that configures Jenkins with HTTPS and Let's Encrypt:
> 
> yaml
> 
> ```yaml
> ---
> # file: roles/jenkins_https/tasks/main.yml
> 
> - name: Install certbot
>   become: yes
>   package:
>     name: certbot
> 
> - name: Obtain SSL certificate
>   become: yes
>   shell: |
>     certbot certonly --standalone -d example.com
>   args:
>     creates: /etc/letsencrypt/live/example.com/fullchain.pem
> 
> - name: Create Systemd service file for Jenkins
>   become: yes
>   copy:
>     dest: /etc/systemd/system/jenkins.service
>     content: |
>       [Unit]
>       Description=Jenkins Continuous Integration Server
>       After=network.target
>   
>       [Service]
>       User=jenkins
>       WorkingDirectory=/var/lib/jenkins
>       ExecStart=/usr/bin/java -jar /usr/share/jenkins/jenkins.war --httpListenAddress=0.0.0.0 --httpPort=8080 --httpsPort=8443 --httpsCertificate=/etc/letsencrypt/live/example.com/fullchain.pem --httpsPrivateKey=/etc/letsencrypt/live/example.com/privkey.pem
>   
>       [Install]
>       WantedBy=multi-user.target
> 
> - name: Reload Systemd
>   become: yes
>   shell: systemctl daemon-reload
> 
> - name: Start and enable Jenkins
>   become: yes
>   service:
>     name: jenkins
>     state: started
>     enabled: yes
> ```
> 
> Note: Replace "example.com" with your domain name. Also, this is just a sample role and you may need to modify it based on your specific requirements and setup.