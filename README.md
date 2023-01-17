# serde_json_yaml

Simple utility script to \_Ser_ialize/\_De_serialize to/from json or yaml

Much of this was created using (ChatGPT)[https://chat.openai.com/chat/b6a927e9-ffcb-4229-8784-79ba3ed8b1dd] as an example application. Minor modifications were made to the

# Build

```bash
docker build -t serde-json-yaml .
```

## Test

```bash
docker run -itd --name serde-json-yaml
```

# Development

Create python virtual environment and activate

```bash
python -m venv .venv
source .venv/bin/activate

# When done
deactivate
```
