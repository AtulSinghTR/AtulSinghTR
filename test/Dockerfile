#FROM golang:1.12-alpine AS build
#
#
##Get the hello world package from a GitHub repository
#RUN go get github.com/golang/example/hello
#WORKDIR /go/src/github.com/golang/example/hello
## Build the project and send the output to /bin/HelloWorld 
#RUN go build -o /bin/HelloWorld
#
#FROM golang:1.12-alpine
##Copy the build's output binary from the previous build container
#COPY --from=build /bin/HelloWorld /bin/HelloWorld
#ENTRYPOINT ["/bin/HelloWorld"]

ARG DOCKER_REGISTRY
ARG LIBRARY_AMAZON_LINUX_VERSION
ARG ARTIFACTORY_USERNAME
ARG ARTIFACTORY_PASSWORD
FROM $DOCKER_REGISTRY/amazonlinux:$LIBRARY_AMAZON_LINUX_VERSION
RUN yum install -y awscli jq java-11-amazon-corretto unzip iproute curl postgresql10 \
  && mkdir -p /opt/product-services/resource \
  && curl -u $ARTIFACTORY_USERNAME:$ARTIFACTORY_PASSWORD https://tr1.jfrog.io/artifactory/libs-snapshot-local/com/tr/akkadia/aws-cdk-akkadia/1.0.0-SNAPSHOT/aws-cdk-akkadia-1.0.0-20210511.185808-16.zip -o /opt/product-services/resource/aws-cdk-akkadia-1.0.0-20210511.185808-16.zip \
  && ls -l
  
#COPY *.zip /opt/product-services/resource/
#RUN ls -l /opt/product-services/resource
