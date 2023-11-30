<html>
<head>
<h1>0x10. Python - Network #0: The WEB and Cookies</h1>
</head>
<p>Internet (or The Web) is a massive distributed client/server information system as depicted in the following diagram.</p>
<img src="https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/images/TheWeb.png" alt="Web">
<p>Many applications are running concurrently over the Web, such as web browsing/surfing, e-mail, file transfer, audio & video streaming, and so on.  In order for proper communication to take place between the client and the server, these applications must agree on a specific application-level protocol such as HTTP, FTP, SMTP, POP, and etc.</p>
<h3>HyperText Transfer Protocol (HTTP)</h3>
<p>HTTP (Hypertext Transfer Protocol) is perhaps the most popular application protocol used in the Internet (or The WEB).</p>
<ul>
<li>HTTP is an asymmetric request-response client-server protocol as illustrated.  An HTTP client sends a request message to an HTTP server.  The server, in turn, returns a response message.  In other words, HTTP is a pull protocol, the client pulls information from the server (instead of server pushes information down to the client).</li>
<img src="https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/images/HTTP.png">
<br>
<li>HTTP is a stateless protocol. In other words, the current request does not know what has been done in the previous requests.</li>
<li>HTTP permits negotiating of data type and representation, so as to allow systems to be built independently of the data being transferred</li>
<li>Quoting from the RFC2616: "The Hypertext Transfer Protocol (HTTP) is an application-level protocol for distributed, collaborative, hypermedia information systems. It is a generic, stateless, protocol which can be used for many tasks beyond its use for hypertext, such as name servers and distributed object management systems, through extension of its request methods, error codes and headers."</li>
</ul>
<br>
<h3>Browser</h3>
<p>Whenever you issue a URL from your browser to get a web resource using HTTP, e.g. http://www.nowhere123.com/index.html, the browser turns the URL into a request message and sends it to the HTTP server. The HTTP server interprets the request message, and returns you an appropriate response message, which is either the resource you requested or an error message. This process is illustrated below:</p>
<br>
<img src="https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/images/HTTP_Steps.png">
<br>
<h3>Uniform Resource Locator (URL)</h3>
<p>A URL (Uniform Resource Locator) is used to uniquely identify a resource over the web. URL has the following syntax:</p>
<pre>
```
protocol://hostname:port/path-and-file-name
```
</pre>
<p>There are 4 parts in a URL:</p>
<ol>
<li>Protocol: The application-level protocol used by the client and server, e.g., HTTP, FTP, and telnet.</li>
<li>Hostname: The DNS domain name (e.g., www.nowhere123.com) or IP address (e.g., 192.128.1.2) of the server.</li>
<li>Port: The TCP port number that the server is listening for incoming requests from the clients.</li>
<li>Path-and-file-name: The name and location of the requested resource, under the server document base directory.</li>
</ol>
<p>For example, in the URL http://www.nowhere123.com/docs/index.html, the communication protocol is HTTP; the hostname is www.nowhere123.com. The port number was not specified in the URL, and takes on the default number, which is TCP port 80 for HTTP. The path and file name for the resource to be located is "/docs/index.html".</p>
<p>Other examples of URL are:</p>
<pre>
```
ftp://www.ftp.org/docs/test.txt
mailto:user@test101.com
news:soc.culture.Singapore
telnet://www.nowhere123.com/
```
</pre>
<h3>HTTP Protocol</h3>
<p>As mentioned, whenever you enter a URL in the address box of the browser, the browser translates the URL into a request message according to the specified protocol; and sends the request message to the server.</p>
<p>For example, the browser translated the URL http://www.nowhere123.com/doc/index.html into the following request message:</p>
<pre>
```
GET /docs/index.html HTTP/1.1
Host: www.nowhere123.com
Accept: image/gif, image/jpeg, */*
Accept-Language: en-us
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)
(blank line)
```
</pre>
<p>When this request message reaches the server, the server can take either one of these actions:</p>
<ol>
<li>The server interprets the request received, maps the request into a file under the server's document directory, and returns the file requested to the client.</li>
<li>The server interprets the request received, maps the request into a program kept in the server, executes the program, and returns the output of the program to the client.</li>
<li>The request cannot be satisfied, the server returns an error message.</li>
</ol>
<p>An example of the HTTP response message is as shown:</p>
<pre>
```
HTTP/1.1 200 OK
Date: Sun, 18 Oct 2009 08:56:53 GMT
Server: Apache/2.2.14 (Win32)
Last-Modified: Sat, 20 Nov 2004 07:16:26 GMT
ETag: "10000000565a5-2c-3e94b66c2e680"
Accept-Ranges: bytes
Content-Length: 44
Connection: close
Content-Type: text/html
X-Pad: avoid browser bug

<html><body><h1>It works!</h1></body></html>
```
</pre>
<p>The browser receives the response message, interprets the message and displays the contents of the message on the browser's window according to the media type of the response (as in the Content-Type response header). Common media type include "text/plain", "text/html", "image/gif", "image/jpeg", "audio/mpeg", "video/mpeg", "application/msword", and "application/pdf".</p>
<p>In its idling state, an HTTP server does nothing but listening to the IP address(es) and port(s) specified in the configuration for incoming request. When a request arrives, the server analyzes the message header, applies rules specified in the configuration, and takes the appropriate action. The webmaster's main control over the action of web server is via the configuration, which will be dealt with in greater details in the later sections.</p>
<br>
<h2>Using HTTP cookies</h2>
<p>An HTTP cookie (web cookie, browser cookie) is a small piece of data that a server sends to a user's web browser. The browser may store the cookie and send it back to the same server with later requests. Typically, an HTTP cookie is used to tell if two requests come from the same browser—keeping a user logged in, for example. It remembers stateful information for the stateless HTTP protocol.</p>
<p>Cookies are mainly used for three purposes:

Session management
Logins, shopping carts, game scores, or anything else the server should remember

Personalization
User preferences, themes, and other settings

Tracking
Recording and analyzing user behavior</p>
<h5>Creating cookies</h5>
<p>After receiving an HTTP request, a server can send one or more Set-Cookie headers with the response. The browser usually stores the cookie and sends it with requests made to the same server inside a Cookie HTTP header. You can specify an expiration date or time period after which the cookie shouldn't be sent. You can also set additional restrictions to a specific domain and path to limit where the cookie is sent.</p>
<h6>The Set-Cookie and Cookie headers</h6>
<p>The Set-Cookie HTTP response header sends cookies from the server to the user agent. A simple cookie is set like this:</p>
<pre>
```
HTTP
Set-Cookie: <cookie-name>=<cookie-value>
```
</pre>
<pre>
```
HTTP
HTTP/2.0 200 OK
Content-Type: text/html
Set-Cookie: yummy_cookie=choco
Set-Cookie: tasty_cookie=strawberry
```
</pre>

<p>Then, with every subsequent request to the server, the browser sends all previously stored cookies back to the server using the Cookie header.</p>
<pre>
```
HTTP
GET /sample_page.html HTTP/2.0
Host: www.example.org
Cookie: yummy_cookie=choco; tasty_cookie=strawberry
```
</pre>
</html>