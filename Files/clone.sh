GITREPO=$2
NAME=$1
LAUNCH_PARMS=$3
SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )" #get script location
REPODIR=$SCRIPTPATH/../Repos/$NAME                
DOCKERFILE=$REPODIR/../../Files/Dockerfiles/$NAME

runcontainer () { docker run -it --rm --name $NAME $NAME:latest $LAUNCH_PARMS; }

git clone $GITREPO $REPODIR
rm $REPODIR/Dockerfile     #Remove repo old Dockerfile
touch $REPODIR/Dockerfile  #Recreate a new Dockerfile
cat  $DOCKERFILE >> $REPODIR/Dockerfile  #Write Dockerfile content
docker build -t $NAME $REPODIR  #Build the image

while true; do
    runcontainer
    read -p "Run again (y/n) ? : " yn
    case $yn in
        [Yy]* ) echo "ok again";;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no.";;
    esac
done
echo "Press Ctrl+C to exit"
$SHELL