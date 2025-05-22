FROM golang:1.22-alpine as builder
WORKDIR /app
COPY ../sincronizacao-go /app
RUN go build -o main .
FROM alpine:latest
WORKDIR /root/
COPY --from=builder /app/main .
EXPOSE 8080
CMD ["./main"]