import os


os.system(' curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
os.system("chmod +x /usr/local/bin/docker-compose")
os.system("cp docker-compose.yml /") 
os.system("cd / ")
os.system("mkdir /folder")
os.system("cd /folder/")
os.system("pwd")
os.system("mv ../docker-compose.yml .")
os.system("docker-compose up -d")