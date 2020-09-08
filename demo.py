import docker, os


client = docker.DockerClient(base_url='tcp://192.168.45.10:2375')

current_dir = '/vagrant'

nginx_ports = {
  '80/tcp': 8080
}

nginx_volumes = {
  f'{current_dir}/index.html': {
    'bind': '/usr/share/nginx/html/index.html',
    'mode': 'ro'
  }
}

nginx_container = client.containers.run(
  image="nginx:1.17",
  ports=nginx_ports,
  volumes=nginx_volumes,
  remove=True,
  detach=True)

nginx_container.logs()
