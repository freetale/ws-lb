use rand::prelude::*;
use std::net::TcpListener;
use std::thread::spawn;
use tungstenite::accept;

/// A WebSocket echo server
fn main() {
    let server = TcpListener::bind("0.0.0.0:9001").unwrap();
    for stream in server.incoming() {
        spawn(move || {
            let usteam = stream.unwrap();
            let addr: std::net::SocketAddr = usteam.peer_addr().unwrap();
            println!("{}", addr);
            let mut websocket = accept(usteam).unwrap();
            loop {
                let msg = match websocket.read() {
                    Ok(x) => x,
                    Err(_) => break,
                };
                // if msg.is_text() {
                //     println!("{}", msg.to_string())
                // }
                // We do not want to send back ping/pong messages.
                if msg.is_binary() || msg.is_text() {
                    websocket.send(msg).unwrap();
                }
            }
        });
    }
}
