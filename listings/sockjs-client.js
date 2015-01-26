var sock = new SockJS('http://example.com/echo');

sock.onopen = function() {
    console.log('open');
    sock.send('Echo Test');
};

sock.onmessage = function(e) {
    console.log('message', e.data);
};

sock.onclose = function() {
    console.log('close');
};
 
 