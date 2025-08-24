import streamlit as st
import random
import time
from PIL import Image, ImageDraw

st.set_page_config(page_title="🐢 Turtle Race", layout="centered")

st.title("🐢 Turtle Grand Prix")
st.write("Enjoy smooth graphics, random winner, and real turtles racing!")

# Turtle colors
turtle_colors = ["red", "green", "purple", "blue", "orange"]

# User selection
user_choice = st.radio("Pick your turtle:", turtle_colors, horizontal=True)

# Track settings
track_width = 600
track_height = 300
finish_line = track_width - 80

# Load or create turtle images (here we’ll just use colored circles as turtles)
def draw_track(turtles_pos):
    img = Image.new("RGB", (track_width, track_height), "white")
    draw = ImageDraw.Draw(img)

    # Draw start & finish lines
    draw.line((60, 0, 60, track_height), fill="black", width=4)
    draw.line((finish_line, 0, finish_line, track_height), fill="black", width=4)

    # Draw lanes and turtles
    lane_height = track_height // len(turtle_colors)
    for i, color in enumerate(turtle_colors):
        y = i * lane_height + lane_height // 2

        # Lane separator
        if i > 0:
            draw.line((0, i * lane_height, track_width, i * lane_height), fill="gray", width=1)

        # Turtle (circle)
        x = turtles_pos[color]
        draw.ellipse((x, y-15, x+30, y+15), fill=color, outline="black")

    return img

if st.button("Start Race 🚦"):
    turtles_pos = {c: 60 for c in turtle_colors}  # all turtles start at x=60
    race_area = st.empty()
    winner = None

    while not winner:
        # Move turtles randomly
        for color in turtle_colors:
            turtles_pos[color] += random.randint(5, 15)
            if turtles_pos[color] >= finish_line:
                winner = color
                break

        # Draw current frame
        frame = draw_track(turtles_pos)
        race_area.image(frame, use_container_width=True)
        time.sleep(0.2)

    # Show result
    if user_choice == winner:
        st.success(f"🏆 Winner: {winner.capitalize()} — You guessed right!")
    else:
        st.error(f"🏁 Winner: {winner.capitalize()} — Better luck next time!")
