import time
import shutil


def format_interval(time):
    """
        Returns a string in the format 'hh:mm:ss'.
        Excepts a time in seconds
    """
    time = int(time)

    hours = time // 3600
    remaining_seconds = time % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    if hours:
        return f"{hours}:{minutes:02d}:{seconds:02d}"
    return f"{minutes:02d}:{seconds:02d}"


def progress_bar(value, width):
    """
        Retruns a visual 'block' bar.
        Expects a float normalized progress value
    """
    blocks = ["", "▏", "▎", "▍", "▌", "▋", "▊", "▉", "█"]

    total_blocks = value * width
    full_blocks = int(total_blocks)
    fractional_part = total_blocks - full_blocks

    bar = full_blocks * blocks[-1]
    bar += blocks[max(0, min(8, round(fractional_part * 8)))]
    bar += " " * (width - len(bar))

    return bar


def ft_tqdm(lst: range) -> None:
    """
        Library 'tqdm' method rewritten
    """
    iterations = len(lst)
    start = time.time()
    remaining = 0
    speed = 0.0
    last_update = time.time()
    last_print = time.time()

    current_iteration = 0
    for item in lst:
        current_iteration += 1

        terminal_width = shutil.get_terminal_size().columns

        now = time.time()
        if (now - last_update):
            speed = 0.3 / (now - last_update) + (1 - 0.3) * speed
        remaining = (iterations - current_iteration) / speed
        if now - last_print > 0.1 or item == lst[-1]:
            progress_pct = current_iteration / iterations

            left_bar = f"{int(progress_pct * 100):3}%|"

            right_bar = f"|{current_iteration}/{iterations} "
            right_bar += f"[{format_interval(now - start)}"
            right_bar += f"<{format_interval(remaining)}, "
            right_bar += f"{speed:.2f}it/s]"

            progress_bar_width = max(
                1, terminal_width - len(left_bar) - len(right_bar) - 1)

            bar = f"{int(progress_pct * 100):3}%"
            bar += f"|{progress_bar(progress_pct, progress_bar_width)}| "
            bar += f"{current_iteration}/{iterations} "
            bar += f"[{format_interval(now - start)}"
            bar += f"<{format_interval(remaining)}, "
            bar += f"{speed:.2f}it/s]\033[?25l"

            # print(left_bar, right_bar, end="\r", flush=True)

            print(bar, end="\r", flush=True)
            last_print = now
        last_update = now
        yield item


if __name__ == "__main__":
    ft_tqdm(10)
