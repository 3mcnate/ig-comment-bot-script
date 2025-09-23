echo "Paste your copied cURL request from chrome, then press Ctrl+D:"
read -d '' curl_cmd < /dev/tty
rest=$(echo "$curl_cmd" | tail -n +2)

new_cmd="curl -o /dev/null -s -w "%{http_code}" 'https://www.instagram.com/graphql/query'"
final_cmd="$new_cmd
$rest"

for ((i = 0; i < 5000; i++)); do
	status_code=$(eval "$final_cmd")

	if [[ "$status_code" != "200" ]]; then
		echo "Successfully sent $i before getting an error: $status_code"
		echo "Try copy/pasting the request again and rerunning this command" 
		break
	fi
	echo "$i: success"

done