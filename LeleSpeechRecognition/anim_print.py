import time


def anim_print(value, delay=0.25, loop=1, final=' '):
    value_list = [x for x in value]  # 将输入的文本转换为字符列表
    i = 1
    while i <= loop:  # 循环指定的次数
        for char in value_list:
            print(f"\r{char}", end='', flush=True)  # 使用ANSI转义序列覆盖输出当前字符
            time.sleep(delay)  # 延时一段时间
        i += 1
    if final == ' ':
        print(f"\r{final}\b", end='', flush=True)  # 输出最终字符并退格
    else:
        print(f"\r{final}\n", end='', flush=True)  # 输出最终字符并换行
