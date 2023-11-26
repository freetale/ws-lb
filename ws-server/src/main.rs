//! A simple echo server.
//!
//! You can test this out by running:
//!
//!     cargo run --example echo-server 127.0.0.1:12345
//!
//! And then in another window run:
//!
//!     cargo run --example client ws://127.0.0.1:12345/
//!
//! Type a message into the client window, press enter to send it and
//! see it echoed back.

use std::{env, io::Error, time::Duration};

use futures_util::{SinkExt, StreamExt};
use log::info;
use tokio::net::{TcpListener, TcpStream};
use tokio_tungstenite::tungstenite::Result;

#[tokio::main]
async fn main() -> Result<(), Error> {
    let _ = env_logger::try_init();
    let addr = env::args()
        .nth(1)
        .unwrap_or_else(|| "0.0.0.0:9001".to_string());

    // Create the event loop and TCP listener we'll accept connections on.
    let try_socket = TcpListener::bind(&addr).await;
    let listener = try_socket.expect("Failed to bind");
    info!("Listening on: {}", addr);
    println!("starting");

    while let Ok((stream, _)) = listener.accept().await {
        tokio::spawn(accept_connection(stream));
    }

    Ok(())
}

async fn accept_connection(stream: TcpStream) {
    let addr = stream
        .peer_addr()
        .expect("connected streams should have a peer address");
    info!("Peer address: {}", addr);
    let ws_stream = tokio_tungstenite::accept_async(stream)
        .await
        .expect("Error during the websocket handshake occurred");

    info!("New WebSocket connection: {}", addr);

    let (mut write, mut read) = ws_stream.split();
    // let mut interval = tokio::time::interval(Duration::from_millis(10000));

    loop {
        const TIMEOUT_MILLI: u64 = 10000; // 10sec
        let t = tokio::time::timeout(Duration::from_millis(TIMEOUT_MILLI), read.next());
        let msg = t.await.unwrap().unwrap().unwrap();
        if msg.is_text() || msg.is_binary() {
            write.send(msg).await.unwrap();
            // write.send(msg).await.unwrap();
        } else if msg.is_close() {
            break;
        }
    }
}
