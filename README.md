# Playground

Simple Flask project using routing features
- Using only 1 template
- Different endpoints:
  localhost:5001
  localhost:5001/play  # creates 3 boxes
  localhost:5001/play/<num> # creates <num> of boxes
  localhost:5001:/play/<num>/<color>  # creates <num> of boxes and sets background color (e.g. green, blue, purplem, etc.)
