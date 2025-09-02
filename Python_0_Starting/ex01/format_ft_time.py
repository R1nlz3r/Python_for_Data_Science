import time

s = time.time()
# , Thousands separator		. Precision
# f Fixed-point notation	e Scientific notation
print(
    f"Seconds since January 1, 1970: {s:,.4f} \
    or {s:.2e} in scientific notation"
)
# %b Month name
# %d Day of the month in number
# % Year in number
print(f"{time.strftime('%b %d %Y')}")
