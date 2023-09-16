from display import Display
import time

def renderText(display, row, text):
    currentCol = 0
    for letter in text:
        display.set_char_in_cell(row, currentCol, letter)
        currentCol += 1

def program(display):
    renderText(display, 1, "EmuDisplay v0.1")
    renderText(display, 2, "----------------")
    renderText(display, 3, "Debug:")

    # Calculate and display the current FPS
    fps = display.clock.get_fps()
    renderText(display, 5, f"FPS: {fps:.2f}")

    # Calculate and display the current time in seconds
    current_time = time.time() - display.start_time
    renderText(display, 7, f"Time: {current_time:.2f} s")

    # Display a custom message
    renderText(display, 9, "It just works!")

if __name__ == "__main__":
    display = Display(grid_size=(40, 24), cell_size=15)
    display.current_bg_color = display.COLORS["BLACK"]
    display.current_fg_color = display.COLORS["WHITE"]
    display.start_time = time.time()  # Record the program start time
    display.run(program)
