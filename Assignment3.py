parentheses_mapping = {
    "(": ")",
    "{": "}",
    "[": "]"
}


def is_symmetric(trial: str) -> bool:
    stack = []

    for char in trial:
        if char in parentheses_mapping:
            stack.append(char)

        elif char in parentheses_mapping.values():
            if not stack or char != parentheses_mapping[stack.pop()]:
                return False

    return not stack


if __name__ == "__main__":
    assert is_symmetric("( ){[ 1 ]( 1 + 3 )( ){ }}") is True
    assert is_symmetric("( 23 ( 2 - 3)") is False
    assert is_symmetric("( 11 }") is False
