import anthropic
import pyautogui
import io
import base64
key = open("key.txt", "r").read().strip()

client = anthropic.Anthropic(api_key=key)
messages = [{"role": "user", "content": "Save a picture of a cat to my desktop."}]

response = client.beta.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    tools=[
        {
          "type": "computer_20241022",
          "name": "computer",
          "display_width_px": 1920,
          "display_height_px": 1080,
          "display_number": 1,
        },
        {
          "type": "text_editor_20241022",
          "name": "str_replace_editor"
        },
        {
          "type": "bash_20241022",
          "name": "bash"
        }
    ],
    messages=messages,
    betas=["computer-use-2024-10-22"],
)
print(response.content[0].text)
messages.append({"role": "assistant", "content": response.content[0].text})

try:
    screenshot = pyautogui.screenshot()
    buffered = io.BytesIO()
    screenshot.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    
    result = {
                "tool_name": "computer",
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": "image/png",
                    "data": img_str
                }
    }
    print(f"Screenshot taken: {result}")
except Exception as e:
    print(f"Screenshot error: {str(e)}")
    raise

messages.append({"role": "user", "content": result})
response = client.beta.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=messages,
)
print(response)
