> Join the waitlist for [NeuralVox](https://forms.gle/HA4dvRB9nz2G1s2LA) - full-cast AI audiobooks!

# NeuralVox Chatterbox (WIP)

Very experimental script to generate audioplay from a script.

This is a potential step in creating the [NeuralVox platform](https://neuralvox.github.io/), but the final architectural design has not been finalized.

## Install

```
pip install chatterbox-server[server]
chatterbox-server --host 0.0.0.0
```

Create `.env` file with `CHATTERBOX_API_URL` set. If you are running the server locally, you can set content to `CHATTERBOX_API_URL=http://localhost:5000`.

## Usage

Script format:

```
SPEAKER: LINE
```

Make sure you have `<speaker>.mp3` in the directory you are running the script from.

Example script:

```
NARRATOR: Hello, this is the narrator.
JOHN: Hello, this is John.
MARY: Hello, this is Mary.
```

You would need to have `narrator.mp3`, `john.mp3`, and `mary.mp3` in the directory you are running the script from.

File tree example:

```
.
├── main.py
├── script.txt
├── narrator.mp3
├── john.mp3
└── mary.mp3
```
