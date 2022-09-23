class Displayable(object):
    # Class that use display
    # the amount of detail is controlled by max_display_level

    max_display_level = 1

    def display(self, level, **args, **nargs):
        # print the arguments
        if level <= self.max_display_level:
            print(*args, **nargs)

    def visualize(func):
        return func

