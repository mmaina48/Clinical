document.addEventListener('DOMContentLoaded', () => {
    // var socket = io();
    var socket = io.connect('http://'+ document.domain + ':' + location.port);

    socket.on('connect', () => {
        socket.send("Connected!!");
    });
    socket.on('message', data => {
        const p = document.createElement('p');
        const br = document.createElement('br');
        p.innerHTML=data;
        document.querySelector('#display-message-section').append(p);
        // console.log(`Message Received: ${data}`)

    });
    socket.on('some-event', data => {
        console.log(data);
    });
    
    document.querySelector('#send_message').onclick = () => {
        socket.send(document.querySelector('#user_message').value);
    }
})      