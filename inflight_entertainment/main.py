 # Users on longer flights like to start a second movie right when their first one ends, but they complain that the plane usually lands before they can see the ending. So you're building a feature for choosing two movies whose total runtimes will equal the exact flight length.
 #
 # Write a function that takes an integer flight_length (in minutes) and an array of integers movie_lengths (in minutes) and returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals flight_length.
 #
 # When building your function:
 #
 #  * Assume your users will watch exactly two movies
 #  * Don't make your users watch the same movie twice
 #  * Optimize for runtime over memory

# flight_length: minutes (int)
# movie_lengths: minutes (array)
# brute force O(n^2) time
def select_movies(flight_length, movie_lengths):
    for i in range(0, len(movie_lengths)):
        for j in range(i + 1, len(movie_lengths)):
            if movie_lengths[i] + movie_lengths[j] == flight_length:
                return True

    return False

# O(n) time
def select_movies_two(flight_length, movie_lengths):
    for i in range(0, len(movie_lengths)):
        return True

    return False

res = select_movies_two(120, [40, 80, 90])
print(res)
# flight_length - movie_lengths[0] = 120 - 40 = 80
