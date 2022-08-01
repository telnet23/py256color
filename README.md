# py256color

Convert between 256 colors and RGB.

The implementation is based on [`colour.c`](https://github.com/tmux/tmux/blob/master/colour.c) from tmux.

Usage
-

```python
from py256color import from_rgb, to_rgb

from_rgb(42, 84, 126)  # 24

to_rgb(96)  # (135, 95, 135)
```
