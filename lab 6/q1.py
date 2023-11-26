from collections import deque

def ladderLength(startWord, endWord, wordList):
    # Convert wordList to a set for faster lookup
    wordSet = set(wordList)

    # Check if endWord is not in the dictionary, return 0
    if endWord not in wordSet:
        return 0

    queue = deque([(startWord, 1)])

    while queue:
        currentWord, length = queue.popleft()

        # Iterate through each position in the word
        for i in range(len(currentWord)):
            # Try changing each character at the current position
            for char in 'abcdefghijklmnopqrstuvwxyz':
                newWord = currentWord[:i] + char + currentWord[i+1:]

                # Check if the new word is in the dictionary
                if newWord in wordSet:
                    # Check if we reached the endWord
                    if newWord == endWord:
                        return length + 1
                    # If not, add the new word to the queue
                    queue.append((newWord, length + 1))
                    wordSet.remove(newWord)  # Mark the word as visited to avoid cycles

    # If no transformation sequence is found
    return 0

# Example usage:
startWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

result = ladderLength(startWord, endWord, wordList)
print(result)
