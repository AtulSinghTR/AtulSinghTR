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
FROM $DOCKER_REGISTRY/amazonlinux:$LIBRARY_AMAZON_LINUX_VERSION
RUN yum install -y awscli jq java-11-amazon-corretto unzip iproute \
  && amazon-linux-extras install -y postgresql10 \
  && mkdir -p /opt/product-services/resource
COPY *.zip /opt/product-services/resource/
RUN ls -l /opt/product-services/resource
