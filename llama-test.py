import os
import replicate 

os.environ["REPLICATE_API_TOKEN"] = "r8_"
api = replicate.Client(api_token=os.environ["REPLICATE_API_TOKEN"])

val = input('Query: ')

output = api.run(
    "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
        input={"prompt": val}
    )

print(output)

for item in output:
    print(item, end="")