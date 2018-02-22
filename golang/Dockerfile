FROM registry.hub.docker.com/library/golang:1.9

RUN curl -fsSL -o /usr/local/bin/dep https://github.com/golang/dep/releases/download/v0.4.1/dep-linux-amd64 && chmod +x /usr/local/bin/dep

RUN mkdir -p /go/src/mqtt-poc/
WORKDIR /go/src/mqtt-poc

COPY Gopkg.toml Gopkg.lock ./
# copies the Gopkg.toml and Gopkg.lock to WORKDIR

RUN dep ensure -vendor-only

COPY . /go/src/mqtt-poc

RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .

FROM alpine:latest  
RUN apk --no-cache add ca-certificates

WORKDIR /root/

RUN mkdir -p /root/conf

ADD conf/config.json /root/conf/config.json

COPY --from=0 /go/src/mqtt-poc/app .

ENTRYPOINT ["./app"]