echo "Once you've copied the cURL request from chrome, press enter. Your command automatically gets pasted in here."
read < /dev/tty
curl_cmd=$(pbpaste)
echo "Read command"

rest=$(echo "$curl_cmd" | tail -n +2)

new_cmd="curl -o /dev/null -s -w "%{http_code}" 'https://www.instagram.com/graphql/query' \\"
final_cmd="$new_cmd
$rest"

echo "Starting the bot..."

for ((i = 0; i < 5000; i++)); do
	status_code=$(eval "$final_cmd")

	if [[ "$status_code" != "200" ]]; then
		echo "Successfully sent $i commends before getting an error: $status_code"
		echo "Try copying the request again and rerunning this command"
		echo "If you get error: 302, instagram thinks you're a bot for a while and you'll have to try this with a different account." 
		break
	fi
	echo "$i: success"

done