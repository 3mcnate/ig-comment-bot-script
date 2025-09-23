echo "Copy the cURL request from chrome, then press enter. (your command automatically gets pasted in here)"
read
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
		break
	fi
	echo "$i: success"

done