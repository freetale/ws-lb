FROM rust:1.74.0-buster as builder
WORKDIR /app
RUN cargo init --bin .
COPY Cargo.toml Cargo.lock ./
RUN cargo build --release
COPY ./ ./
RUN touch src/main.rs
RUN cargo build --release

FROM debian:buster-slim as runtime
WORKDIR /app
COPY --from=builder /app/target/release/ws-server /app/app
EXPOSE 9001
ENV RUST_LOG="info"
ENTRYPOINT ["./app"]