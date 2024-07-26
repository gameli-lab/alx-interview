This function returns the pascals triangle. This is how it works:

1. If n is less than or equal to 0, it returns an empty list.
2. It initializes the triangle with the first row [1].
3. It iteratively builds each row by summing adjacent elements from the previous row and appending 1 at the start and end of each row.
4. Finally, it returns the completed Pascal's triangle.
