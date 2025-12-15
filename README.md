# github-action-mailgun-sendmail
Send a mail with mailgun API

## Usage
```yaml
name: ci.yml
on:
  push:
    branches:
      - main
jobs:
  sendmail:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - name: Send mail
        uses: ./
        id: mail
        with:
          api_key: ${{ secrets.MAILGUN_API_KEY }}
          domain: ${{ secrets.MAILGUN_DOMAIN }}
          from: ${{ secrets.MAILGUN_FROM }}
          to: ${{ secrets.MAILGUN_TO }}
          subject: ${{ github.event.head_commit.message }}
          message: '<p>Hello World</p>'
```

## Inputs

| name | required | type | default | description |
|------|----------|------|---------|-------------|
|to|yes|string||recipient of the mail|
|from|yes|string||sender of the mail|
|message|yes|string||html body of the mail|
|subject|yes|string||subject of the mail|
|domain|yes|string||mailgun domain|
|api_key|yes|string||mailgun api key|