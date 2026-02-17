$OpenPopPath = "C:\Users\champuser\OpenPop\OpenPop.dll"
# Loads dll for use
[Reflection.Assembly]::LoadFile($OpenPopPath) | Out-Null

$pop3Client = New-Object OpenPop.Pop3.pop3Client

# Variables for setting up the pop3 server

$server = "PhishPhilterPopServer"
$port = 110
$enableSSL = $false
$username = "phishphilteralice@gmail.com"
$password = "nxgi qixd jxmy eodv"

# Connect to the server
$pop3Client.connect($server, $port, $enableSSL)

if (!$pop3Client.connected){
    throw "Unable to connect to POP3 Client. Connection failed with server $server"
}

$pop3Client.authenticate($username, $password)

#$pop3Client.disconnect()