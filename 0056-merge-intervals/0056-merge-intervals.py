class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        intervals.sort(key=lambda x: x[0])

        output = [intervals[0]]

        for start, end in intervals[1:]:

            lastEnding = output[-1][1]

            if (
                start <= lastEnding
            ):  # if the current elements starting index lies withing the range of the previous range
                output[-1][1] = max(
                    lastEnding, end
                )  # choose the maximum of the endings between previous ending and current ending

            else:
                output.append([start, end])  # if the dont overlap just add that range

        return output
