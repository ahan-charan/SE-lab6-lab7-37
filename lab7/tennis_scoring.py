
def _clean_text(value):
    if not isinstance(value, str):
        return None

    value = value.strip()
    return value if value else None


def _parse_nonnegative_integer(token):
    token = token.strip()

    if not token or not token.isascii() or not token.isdecimal():
        return None

    try:
        return int(token)
    except (ValueError, OverflowError):
        return None


def parse_score(text):
    text = _clean_text(text)

    if text is None:
        return None

    parts = text.split("-")

    if len(parts) != 2:
        return None

    a = _parse_nonnegative_integer(parts[0])
    b = _parse_nonnegative_integer(parts[1])

    if a is None or b is None:
        return None

    return (a, b)


def game_lead(text):
    text = _clean_text(text)

    if text is None:
        return None

    parts = text.split("-")

    if len(parts) != 2:
        return None

    points = {
        "0": 0,
        "15": 1,
        "30": 2,
        "40": 3
    }

    first = parts[0].strip()
    second = parts[1].strip()

    if first not in points or second not in points:
        return None

    return points[first] - points[second]


def set_spread(games_csv):
    games_csv = _clean_text(games_csv)

    if games_csv is None:
        return None

    tokens = games_csv.split(",")
    games = []

    for token in tokens:
        value = _parse_nonnegative_integer(token)

        if value is None:
            return None

        games.append(value)

    if not games:
        return None

    return max(games) - min(games)


def main():
    print("==== Running parse_score ====")
    user_input = input("Enter points won as A-B (e.g. 3-2): ")
    result = parse_score(user_input)

    if result is None:
        print("Invalid score. Enter two non-negative integers separated by '-'.")
    else:
        print("Points A and B:", result)

    print("\n==== Running game_lead ====")
    user_input = input("Enter a game score (e.g. 40-30): ")
    result = game_lead(user_input)

    if result is None:
        print("Invalid game score. Use 0, 15, 30 or 40.")
    else:
        print("Lead in Points:", result)

    print("\n==== Running set_spread ====")
    user_input = input("Enter games won per set as CSV (e.g. 6,4,7): ")
    result = set_spread(user_input)

    if result is None:
        print("Invalid set scores. Enter comma-separated non-negative integers.")
    else:
        print("Spread:", result)


if __name__ == "__main__":
    main()

