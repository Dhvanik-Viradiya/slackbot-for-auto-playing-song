---
title: Slackbot for auto playing song
author: Dhvanik Viradiya
date: 8-July-2022
---

# Slackbot for auto playing song

This slack bot is created in python using slack api along with flask. It will trigger the function written in backend as soon as the new message arrives in slack. Basically this bot is playing the song when a youtube link is arrives as a message in slack.

This player contains some commands to play, pause, next, etc...

-  commands
   -  ;play {song name} (  This command will fetch first video from youtube according to {song name} and add it to queue)
   -  ;pause ( Pause the streaming )
   -  ;resume ( Resume the streaming )
   -  ;next ( skip the current song and jump to next song in the queue)
   -  ;sound++ (Increase sound by 15)
   -  ;sound-- (Decrease sound by 15)

# Setup codebase and installation

- Commands to setup code(repo):
  - git clone <https://github.com/Dhvanik-Viradiya/slackbot-for-auto-playing-song.git>
  - cd slackbot-for-auto-playing-song
  - pip install -r requirements.txt

# How to create a slack bot ?

If you already have created a bot then go to the [configuration of bot](#ConfigurationApp) section

1. Go to <https://api.slack.com/>
1. Click on Create an app

   ![](Aspose.Words.ee9642b8-723d-4e63-8859-c0c97d669060.001.png)

1. Click on From scratch

   ![](Aspose.Words.ee9642b8-723d-4e63-8859-c0c97d669060.002.png)

1. Give the appropriate name and select the workspace where you want to install your app and then click on **Create App**

   ![](Aspose.Words.ee9642b8-723d-4e63-8859-c0c97d669060.003.png)

1. Nice ! Your app is created successfully. Now you can see your app name in the left corner.

   ![](Aspose.Words.ee9642b8-723d-4e63-8859-c0c97d669060.004.png)

<h1 id="ConfigurationApp">
   Configuration of app
</h1>

1. Click on Basic Information and scroll it down to the **App Credentials** section.

   ![](Aspose.Words.ee9642b8-723d-4e63-8859-c0c97d669060.005.png)

1. Copy the **Signing Secret** code and paste it into .env file SIGNING\_SECRET = …

   ![](Aspose.Words.ee9642b8-723d-4e63-8859-c0c97d669060.006.png)

1. Now, scroll up and click on Permissions

   ![](Aspose.Words.ee9642b8-723d-4e63-8859-c0c97d669060.007.png)

1. Scroll down to the **Scopes** section and add an Oauth Scope -> channels:history and chat:write

   ![](Aspose.Words.ee9642b8-723d-4e63-8859-c0c97d669060.008.png)

1. Scroll up and click **Install to Workspace**

   ![](Aspose.Words.ee9642b8-723d-4e63-8859-c0c97d669060.009.png)

1. Click **Allow**

   ![](Aspose.Words.ee9642b8-723d-4e63-8859-c0c97d669060.010.png)

1. Now it will generate **Bot User OAuth Token** which generally starts with xoxb

   ![](Aspose.Words.ee9642b8-723d-4e63-8859-c0c97d669060.011.png)

1. Copy that token and paste it into .env file -> SLACK\_TOKEN = …

1. Open the slack where you bot is now installed and go to the public channel where you want to add your slack bot.
   1. In my case I want to add my SongApp to #jambox channel.
   1. **Note** :- This will only work on public channel.

      ![](Aspose.Words.ee9642b8-723d-4e63-8859-c0c97d669060.012.png)

1. Type **@** so you will see the you app (bot) listed there

   ![](Aspose.Words.ee9642b8-723d-4e63-8859-c0c97d669060.013.png)

1. Click on that and then press enter you will see the dialog box. Just click on **Add to Channel**

   ![](Aspose.Words.ee9642b8-723d-4e63-8859-c0c97d669060.014.png)

1. Bot is added in this channel.

   ![](Aspose.Words.ee9642b8-723d-4e63-8859-c0c97d669060.015.png)

1. Add this channel to the script as well and run that script using **python slackbot.py** and don’t forget to add **#** before the channel name.

   ![](Aspose.Words.ee9642b8-723d-4e63-8859-c0c97d669060.016.png)

1. Your bot is running now on some port number. In my case it is 5000. Note that it will use next.

   ![](Aspose.Words.ee9642b8-723d-4e63-8859-c0c97d669060.017.png)

1. Download the ngrok from <https://ngrok.com/download>

1. Open the ngrok terminal if it installed separate terminal else open the terminal.

1. Type ngrok http {port\_number}

   1. If your flask server is running on 5000 port then it should be **ngrok http 5000

      ![](Aspose.Words.ee9642b8-723d-4e63-8859-c0c97d669060.018.png)**

   1. Here you can use this forwarding link for 2 hours only.

   1. For infinite use of link you must be login to ngrok.

   1. Basically, ngrok will transfer the request to our localhost.

   1. Copy the forwarding url.

1. Now go back to slack api tab and click on **Event Subscription** and Enable Events

   ![](Aspose.Words.ee9642b8-723d-4e63-8859-c0c97d669060.019.png)

   and paste that url to the **Request URL** along with appending this text -> /slack/events. You will see the Verified mark if you follow this documentation carefully.

   ![](Aspose.Words.ee9642b8-723d-4e63-8859-c0c97d669060.020.png)

1. Click on **Subscribe to bot events** and click on **Add Bot User Event.**

   ![](Aspose.Words.ee9642b8-723d-4e63-8859-c0c97d669060.021.png)

1. Add **message.channels** and click on **Save Changes**

   ![](Aspose.Words.ee9642b8-723d-4e63-8859-c0c97d669060.022.png)

1. And finally the slack bot configuration is finished. Your bot is ready. :)
