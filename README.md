for creatin gour own docker images

--first we have to create a folder separately for that docker images 

cd ubuntu-image
code . #to open vs code

write in dockerfile 

to build images

->go to the path where dockerfile  exist then 

--> write into docker file the commands you want to execute 
-->after done build the image 

-> docker build -t bushrajavaimage . 

images list 
-> docker images 
remove image 
-> docker rmi imageid

container list  
-> docker ps -a 

list of  running container 
--> docker ps 

remove conatiner 
-> docker rm  containerid 

docker running image we created

docker run --name bushraPythonContainer1 bushrapythonproject:v1


#run docker image in interactive mode while exposing port 


**step by step approch for making docker image and container**
first make docker image step 1
step 1:

# docker build -t imagenameyouwnattogive(only lower case accepted) .

step 2

withour port

# docker run --name containernameyouwanttogive -it -d  imagename/image id
with port
# docker run --name containernameyouwanttogive -it -d  -p 5000:5000 imagename/image id


step 3

#check if its image is  running or not using command (list of all runnign container)

# docker ps 

step 4
to stop it 

docker stop container name/id







