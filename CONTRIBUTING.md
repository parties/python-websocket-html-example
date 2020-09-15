# Contributing

Pull requests welcome.

## Updating the demo GIF

On Mac:
```
# source: https://superuser.com/a/556031/47533

# 1. Install ffmpeg
brew install ffmpeg

# 2. Create a screen recording using QuicktimePlayer (File > New Screen Recording)

# 3. Optimize using ffmpeg
ffmpeg -i ./websocket-demo.orig.mov ./websocket-demo.optimized.mov

# 4. Create GIF
ffmpeg -i ./websocket-demo.optimized.mov -vf "fps=10,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 ./websocket-demo.gif

# 5. Update gif in this repo
cp ./websocket-demo.gif /path/to/python-websocket-example/docs/resources/websocket-demo.gif
```
