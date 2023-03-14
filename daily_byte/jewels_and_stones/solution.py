def jewels_and_stones(jewels: str, stones: str) -> int:
    return len([stone for stone in stones if stone in jewels])
