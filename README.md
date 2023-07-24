# googletrans

***googletrans*** is a simple translation interface that utilizes Google Translator python library. This script can
simply be integrated into other projects.

## Getting started

1. Clone the repository:
```bash
git clone https://github.com/ali-mohammadi/googletrans.git
```
2. Install the dependencies:
```bash
pip install -r requirements.txt
```
3. Run the script using the `main.py <json>`. You're all set!

### JSON format:
```json
{
  "text": "<input-text>",
  "des": "<language-to>",
  "src": "<language-from> (optional, default: auto)"
}
```

## License

This project is licensed under the [MIT License](LICENSE).