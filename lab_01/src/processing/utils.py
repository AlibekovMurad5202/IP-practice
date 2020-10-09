def clamp_bgr_pixel(colors, value):
    b_result = max(min(colors[0] + value, 255), 0)
    g_result = max(min(colors[1] + value, 255), 0)
    r_result = max(min(colors[2] + value, 255), 0)
    return (b_result, g_result, r_result)