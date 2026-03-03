$OpenPopPath = "C:\Users\champuser\OpenPop\OpenPop.dll"
Unblock-File -Path $OpenPopPath
Add-Type -Path $OpenPopPath
$pop3Client = New-Object OpenPop.Pop3.pop3Client

# Variables for setting up the pop3 server
# Maybe put this in a config file? Make a setup readme

$server = "pop.gmail.com"
$port = 995
$enableSSL = $true
$username = "recent:phishphilteralice@gmail.com"
$secure = Get-Content "C:\Users\champuser\Desktop\AppPassword.txt" | ConvertTo-SecureString
$password = ConvertFrom-SecureString -SecureString $secure -AsPlainText

# Connect to the server
function Connect_Server () {
    $pop3Client.connect($server, $port, $enableSSL)
    if (!$pop3Client.connected){
        throw "Unable to connect to POP3 Client. Connection failed with server $server"
    }
    $pop3Client.authenticate($username, $password)
}

Connect_Server
# Do things here

function Test_Email () {
    # Gets the total number of emails on the client
    $message_num = $pop3Client.GetMessageCount()
    Write-Host($message_num)
    # Gets the most recent email
    $message = $pop3Client.getMessage($message_num)
    # Gets Header Information from Email
    Write-Host "Subject: $($message.Headers.Subject) "
    Write-Host "From: $($message.Headers.From.Address)"
    Write-Host "Date: $($message.Headers.Date)"
    # Gets body of the email, tries plaintext first before falling back on html
    $message_body = $null
    $text = $message.FindAllTextVersions()
    if ($text){
        $message_body = $text[0].GetBodyAsText()

    }
    else {
        $html = $message.FindFirstHtmlVersion()
        if ($html){
            $message_body = $html.GetBodyAsText()
        }
    }
    Write-Host "Body: "
    Write-Host $message_body
}

function Get_Email (){
    $message_num = $pop3Client.GetMessageCount()
    for ($i = 1; $i -le $message_num; $i++) {
        $message = $pop3Client.getMessage($i)

        $text = $message.FindAllTextVersions()
        if ($text){
            $message_body = $text[0].GetBodyAsText()
        }
        else {
            $html = $message.FindFirstHtmlVersion()
            if($html){
                $message_body = $html.GetBodyAsText()
            }
        }

        $emailContents = [pscustomobject]@{
            Subject = $message.Headers.Subject
            Sender = $message.Headers.From.Address
            Date = $message.Headers.Date
            Body = $message_body
        }

        Write-Host $emailContents.Subject
        Write-Host $emailContents.Sender
        Write-Host $emailContents.Date
        Write-Host $emailContents.Body
    }

}

Get_Email

# Ends Session
$pop3Client.Dispose()