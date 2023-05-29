# Sensor Garden Frontend 

Written with Yew in Rust

Statically Hosted in a Kubernetes cluster using nginx

## Deploy steps
1. Run `trunk build --release`
1. Update the Dockerfile  with the files in dist directory. This requires manually updating the hash
1. build the docker image:
```
docker build -t registry.digitalocean.com/cooper-cluster-container-registry/com.cooperkyle.sensorgardenfrontend .
```
1. (Optional) test the docker image
```
docker run -it -p 8080:8080 registry.digitalocean.com/cooper-cluster-container-registry/com.cooperkyle.sensorgardenfrontend
```
1. Push the docker image
```
docker push registry.digitalocean.com/cooper-cluster-container-registry/com.cooperkyle.sensorgardenfrontend
```


**Note to push you will need to auth with to the docker container registry**
