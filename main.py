"""
Module providing functions for encoding strings using iterative and recursive approaches.
"""

def artcode_i(s):
    """
    Retourne la liste de tuples

    """
    if not s:
        return []

    encoded = []
    current_char = s[0]
    count = 1

    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = char
            count = 1

    # Ajouter le dernier groupe
    encoded.append((current_char, count))

    return encoded

def artcode_r(s):
    """
    Retourne la liste de tuples

    """
    if not s:
        return []

    result = []
    stack = [(0, s[0], 1)]  # (index, current_char, count)

    for index in range(1, len(s)):
        if s[index] == stack[-1][1]:
            stack[-1] = (stack[-1][0], stack[-1][1], stack[-1][2] + 1)
        else:
            result.append((stack[-1][1], stack[-1][2]))
            stack[-1] = (index, s[index], 1)

    result.append((stack[-1][1], stack[-1][2]))
    return result

def main():
    """
    Fonction principale qui teste les deux fonctions secondaires.
    """
    test_string = 'MMMMaaacXolloMM'
    print("Codage itératif :", artcode_i(test_string))
    print("Codage simulant récursion :", artcode_r(test_string))

if __name__ == "__main__":
    main()
