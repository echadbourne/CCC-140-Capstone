$OpenPopPath = "C:\Users\champuser\OpenPop\OpenPop.dll"
Unblock-File -Path $OpenPopPath
Add-Type -Path $OpenPopPath
$pop3Client = New-Object OpenPop.Pop3.pop3Client

# Variables for setting up the pop3 server

$server = "pop.gmail.com"
$port = 995
$enableSSL = $true
$username = "phishphilteralice@gmail.com"
$password = Get-Content "C:\Users\champuser\Desktop\AppPassword.txt" | ConvertTo-SecureString

#open the port for the server

# Connect to the server
$pop3Client.connect($server, $port, $enableSSL)

if (!$pop3Client.connected){
    throw "Unable to connect to POP3 Client. Connection failed with server $server"
}

$pop3Client.authenticate($username, $password)

#Do things here
# Gets the total number of emails on the client
$message_num = $pop3Client.GetMessageCount()
# Gets the most recent email
$message = $pop3Client.getMessage($message_num)
# Gets Header Information from Email
Write-Host "Subject: $($message.Headers.Subject) "
Write-Host "From: $($message.Headers.From.Address)"
Write-Host "Date: $($message.Headers.Date)"
# Gets body of the email, tries plaintext first before falling back on html
$message_body = $null
$text = $message.FindAllTextVersions()
if ($text -gt 0){
    $message_body = $text[0].GetBodyAsText()

}
else {
    $html = $message.FindFirstHtmlVersion()
    if ($html -ne $null ){
        $message_body = $html.GetBodyAsText()
    }
}
Write-Host "Body: "
Write-Host $message_body

# Ends Session
$pop3Client.Dispose()