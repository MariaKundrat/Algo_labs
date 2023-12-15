def createStateMachine(needle):
    m = len(needle)
    characters = set(needle)
    transitions = [{c: 0 for c in characters} for _ in range(m + 1)]
    transitions[0][needle[0]] = 1

    x = 0
    for i in range(1, m + 1):
        for c in characters:
            transitions[i][c] = transitions[x][c]
        if i < m:
            transitions[i][needle[i]] = i + 1
            x = transitions[x][needle[i]]

    return transitions


def findNeedle(haystack, needle):
    if not haystack or not needle:
        return -1

    transitions = createStateMachine(needle)
    n = len(haystack)
    m = len(needle)
    currentState = 0
    indices = []

    for i in range(n):
        if haystack[i] in transitions[currentState]:
            currentState = transitions[currentState][haystack[i]]
        else:
            currentState = 0

        if currentState == m:
            indices.append(i - m + 1)

    return indices if indices else -1


haystack = " the apple the mouse"
needle = "the"
result = findNeedle(haystack, needle)
if result != -1:
    print(f"Line '{needle}' - {result} - '{haystack}'.")
else:
    print(f"Line '{needle}' doesn`t exists in '{haystack}'.")
