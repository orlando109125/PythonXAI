# 骰子模擬

import random
import argparse
import sys


def rolldice(n: int) -> list:
    """擲 n 次骰子，回傳結果列表（1-6）。"""
    if n <= 0:
        return []
    return [random.randint(1, 6) for _ in range(n)]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="丟骰子指令 - 回傳所有擲骰子結果")
    parser.add_argument("-n", "--count", type=int, help="擲骰子次數（正整數）")
    args = parser.parse_args()

    try:
        if args.count is not None:
            n = args.count
        else:
            s = input("請輸入擲骰子次數: ")
            n = int(s.strip())
        if n < 0:
            raise ValueError
    except Exception:
        print("輸入不正確，請輸入正整數。")
        sys.exit(1)
    else:
        results = roll_dice(n)
        print("擲骰子結果：", results)
