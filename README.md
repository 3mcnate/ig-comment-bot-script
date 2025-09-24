# IG bot

## How to use

>Note: this only works on mac for now.

1. Open Terminal on your computer (do a spotlight search for Terminal)
2. copy and paste this command and hit enter ONCE: 

```bash
curl -s "https://raw.githubusercontent.com/3mcnate/ig-comment-bot-script/refs/heads/main/script.zsh" | zsh
```

3. Open the post on Chrome: <https://www.instagram.com/p/DO6saVckhMQ/>
4. Make sure you're logged in
5. Right click anywhere on the screen and click "Inspect"
6. Open the "Network" tab
7. Make a comment on the post.
8. You should see a line pop up in the network tab called "query". Right click on it, then select Copy > Copy as cURL.
9. Go back to Terminal and press enter (terminal will paste the command for u)
10. Watch the comments roll in
 
**Important**: while the bot is running, don't log out of instagram on your computer! If you do, you have to repeat the process.
